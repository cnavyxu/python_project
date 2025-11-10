# Docker 部署文档

## 概述

本文档介绍如何使用 Docker 和 Docker Compose 部署算法与模型 API 服务。

## 前置要求

- Docker >= 20.10
- Docker Compose >= 2.0（可选，用于编排）

## 快速开始

### 使用 Docker Compose（推荐）

```bash
# 启动服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f api

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 停止并删除所有容器和网络
docker-compose down -v
```

### 使用 Docker 命令

```bash
# 构建镜像
docker build -t algo-models:latest .

# 运行容器
docker run -d \
  --name algo-models-api \
  -p 8000:8000 \
  -v $(pwd)/logs:/app/logs \
  -v $(pwd)/data:/app/data \
  -e LOG_LEVEL=INFO \
  algo-models:latest

# 查看日志
docker logs -f algo-models-api

# 停止容器
docker stop algo-models-api

# 删除容器
docker rm algo-models-api
```

## 镜像构建

### 基础构建

```bash
./scripts/docker_build.sh
```

或手动构建：

```bash
docker build -t algo-models:latest .
```

### 构建特定版本

```bash
docker build -t algo-models:v1.0.0 .
```

### 多阶段构建（可选优化）

如果需要更小的镜像，可以使用多阶段构建。编辑 `Dockerfile`：

```dockerfile
# 构建阶段
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 运行阶段
FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Docker Compose 配置详解

### 基本配置

```yaml
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: algo-models-api
    ports:
      - "8000:8000"
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data
    environment:
      - LOG_LEVEL=INFO
      - PYTHONPATH=/app
    restart: unless-stopped
    networks:
      - algo-network

networks:
  algo-network:
    driver: bridge
```

### 添加 Redis 缓存

```yaml
version: '3.8'

services:
  api:
    build: .
    container_name: algo-models-api
    ports:
      - "8000:8000"
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
    depends_on:
      - redis
    networks:
      - algo-network

  redis:
    image: redis:7-alpine
    container_name: algo-models-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - algo-network

networks:
  algo-network:
    driver: bridge

volumes:
  redis_data:
```

### 添加 Nginx 反向代理

```yaml
version: '3.8'

services:
  api:
    build: .
    container_name: algo-models-api
    expose:
      - "8000"
    networks:
      - algo-network

  nginx:
    image: nginx:alpine
    container_name: algo-models-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - api
    networks:
      - algo-network

networks:
  algo-network:
    driver: bridge
```

Nginx 配置示例 (`nginx.conf`)：

```nginx
events {
    worker_connections 1024;
}

http {
    upstream api {
        server api:8000;
    }

    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://api;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

## 环境变量

可以通过环境变量配置服务：

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| LOG_LEVEL | 日志级别 | INFO |
| PYTHONPATH | Python 模块路径 | /app |
| API_HOST | API 监听地址 | 0.0.0.0 |
| API_PORT | API 监听端口 | 8000 |

### 使用 .env 文件

创建 `.env` 文件：

```bash
LOG_LEVEL=DEBUG
API_PORT=8000
```

Docker Compose 会自动加载。

## 数据持久化

### 日志持久化

```yaml
volumes:
  - ./logs:/app/logs
```

日志将保存在主机的 `logs/` 目录。

### 数据持久化

```yaml
volumes:
  - ./data:/app/data
```

数据文件将保存在主机的 `data/` 目录。

### 使用命名卷

```yaml
services:
  api:
    volumes:
      - logs_data:/app/logs
      - app_data:/app/data

volumes:
  logs_data:
  app_data:
```

## 健康检查

### Dockerfile 中的健康检查

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1
```

### Docker Compose 中的健康检查

```yaml
services:
  api:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
```

查看健康状态：

```bash
docker ps
# 或
docker inspect --format='{{json .State.Health}}' algo-models-api
```

## 日志管理

### 查看日志

```bash
# Docker Compose
docker-compose logs -f
docker-compose logs -f api
docker-compose logs --tail=100 api

# Docker
docker logs -f algo-models-api
docker logs --tail=100 algo-models-api
docker logs --since 30m algo-models-api
```

### 日志驱动配置

在 `docker-compose.yml` 中配置：

```yaml
services:
  api:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

## 生产环境部署

### 1. 使用外部配置

```yaml
services:
  api:
    env_file:
      - .env.production
    volumes:
      - ./config.prod.yaml:/app/config.yaml:ro
```

### 2. 设置资源限制

```yaml
services:
  api:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G
```

### 3. 配置重启策略

```yaml
services:
  api:
    restart: always
    # 或
    # restart: on-failure:3
```

### 4. 使用 Docker Swarm

```bash
# 初始化 Swarm
docker swarm init

# 部署服务
docker stack deploy -c docker-compose.yml algo-models

# 查看服务
docker service ls
docker service ps algo-models_api

# 扩展服务
docker service scale algo-models_api=3

# 删除服务
docker stack rm algo-models
```

### 5. 使用 Kubernetes

创建 `k8s-deployment.yaml`：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: algo-models-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: algo-models-api
  template:
    metadata:
      labels:
        app: algo-models-api
    spec:
      containers:
      - name: api
        image: algo-models:latest
        ports:
        - containerPort: 8000
        env:
        - name: LOG_LEVEL
          value: "INFO"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 30
        resources:
          limits:
            memory: "2Gi"
            cpu: "1000m"
---
apiVersion: v1
kind: Service
metadata:
  name: algo-models-service
spec:
  selector:
    app: algo-models-api
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8000
  type: LoadBalancer
```

部署：

```bash
kubectl apply -f k8s-deployment.yaml
kubectl get pods
kubectl get services
```

## 监控和维护

### 查看资源使用

```bash
# 实时资源使用
docker stats

# 特定容器
docker stats algo-models-api

# Docker Compose
docker-compose stats
```

### 清理未使用资源

```bash
# 清理停止的容器
docker container prune

# 清理未使用的镜像
docker image prune -a

# 清理未使用的卷
docker volume prune

# 全部清理
docker system prune -a --volumes
```

### 备份和恢复

#### 备份数据卷

```bash
docker run --rm \
  -v algo-models_logs_data:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/logs-backup.tar.gz -C /data .
```

#### 恢复数据卷

```bash
docker run --rm \
  -v algo-models_logs_data:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/logs-backup.tar.gz -C /data
```

## 故障排查

### 容器无法启动

```bash
# 查看容器日志
docker logs algo-models-api

# 查看容器详细信息
docker inspect algo-models-api

# 进入容器调试
docker exec -it algo-models-api /bin/bash
```

### 网络问题

```bash
# 查看网络
docker network ls
docker network inspect algo-network

# 测试容器间连接
docker exec algo-models-api ping redis
```

### 端口冲突

```bash
# 查看端口占用
sudo lsof -i :8000
# 或
sudo netstat -tulpn | grep 8000

# 修改端口映射
# docker-compose.yml
ports:
  - "8001:8000"
```

## 安全建议

1. **不要以 root 用户运行**
   ```dockerfile
   RUN useradd -m -u 1000 appuser
   USER appuser
   ```

2. **使用 secrets 管理敏感信息**
   ```yaml
   services:
     api:
       secrets:
         - api_key
   
   secrets:
     api_key:
       file: ./secrets/api_key.txt
   ```

3. **扫描镜像漏洞**
   ```bash
   docker scan algo-models:latest
   ```

4. **限制容器权限**
   ```yaml
   services:
     api:
       security_opt:
         - no-new-privileges:true
       cap_drop:
         - ALL
   ```

5. **使用只读文件系统**
   ```yaml
   services:
     api:
       read_only: true
       tmpfs:
         - /tmp
   ```

## 性能优化

1. **使用更小的基础镜像**（alpine, slim）
2. **多阶段构建**减小镜像大小
3. **.dockerignore** 排除不必要的文件
4. **缓存 pip 包**加速构建
5. **使用 volume** 而非 bind mount 提高性能

## 参考资源

- [Docker 官方文档](https://docs.docker.com/)
- [Docker Compose 文档](https://docs.docker.com/compose/)
- [FastAPI 部署指南](https://fastapi.tiangolo.com/deployment/)
- [Python Docker 最佳实践](https://docs.docker.com/language/python/)
