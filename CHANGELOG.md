# 更新日志

## [0.2.0] - 2024-11-10

### 新增功能

#### 1. 日志模块 (src/logging/)
- ✅ 统一的日志配置和管理
- ✅ 支持控制台和文件输出
- ✅ 支持日志轮转（按大小和时间）
- ✅ 可自定义日志格式和级别
- ✅ 为不同模块创建独立 Logger
- ✅ 完整的测试覆盖
- 📖 详细文档: [docs/LOGGING.md](docs/LOGGING.md)

**使用示例：**
```python
from src.logging import get_logger

logger = get_logger(__name__)
logger.info("这是一条日志信息")
```

#### 2. API 服务模块 (src/api/)
- ✅ 基于 FastAPI 的 REST API 服务
- ✅ 支持算法调用（排序、搜索）
- ✅ 支持模型训练和预测（线性回归、KNN）
- ✅ 自动生成 API 文档（Swagger UI / ReDoc）
- ✅ 健康检查端点
- ✅ 全局异常处理
- ✅ CORS 支持
- ✅ 完整的测试覆盖
- 📖 详细文档: [docs/API_USAGE.md](docs/API_USAGE.md)

**启动服务：**
```bash
./scripts/start_api.sh
# 或
docker-compose up -d
```

**API 端点：**
- `GET /health` - 健康检查
- `POST /api/v1/algorithms/sort` - 数组排序
- `POST /api/v1/algorithms/search` - 数组搜索
- `POST /api/v1/models/train` - 模型训练
- `POST /api/v1/models/predict` - 模型预测
- `GET /docs` - API 文档

#### 3. Docker 部署模块
- ✅ Dockerfile - 构建 Python 应用镜像
- ✅ docker-compose.yml - 服务编排
- ✅ .dockerignore - 优化镜像大小
- ✅ 健康检查配置
- ✅ 数据持久化支持
- ✅ 启动脚本
- 📖 详细文档: [docs/DOCKER_DEPLOYMENT.md](docs/DOCKER_DEPLOYMENT.md)

**快速部署：**
```bash
# 使用 Docker Compose
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

### 更新内容

#### 依赖更新
- ➕ fastapi>=0.104.0
- ➕ uvicorn[standard]>=0.24.0
- ➕ pydantic>=2.5.0

#### 文档
- 📝 新增 API 使用文档
- 📝 新增日志模块文档
- 📝 新增 Docker 部署文档
- 📝 更新主 README

#### 示例代码
- 📄 logging_example.py - 日志模块使用示例
- 📄 api_client_example.py - API 客户端使用示例

#### 测试
- ✅ tests/test_logging.py - 日志模块测试 (7 个测试)
- ✅ tests/test_api.py - API 服务测试 (17 个测试)

#### 脚本
- 🔧 scripts/start_api.sh - API 服务启动脚本
- 🔧 scripts/docker_build.sh - Docker 镜像构建脚本

### 项目结构变化

```diff
src/
+ ├── logging/              # 日志模块
+ │   ├── __init__.py
+ │   └── logger.py
+ └── api/                  # API 服务模块
+     ├── __init__.py
+     ├── app.py
+     ├── schemas.py
+     └── routes/
+         ├── __init__.py
+         ├── health.py
+         ├── algorithms.py
+         └── models.py
```

### 使用指南

1. **本地开发**
   ```bash
   # 安装依赖
   pip install -r requirements.txt
   
   # 启动 API 服务
   ./scripts/start_api.sh
   ```

2. **Docker 部署**
   ```bash
   # 构建并启动
   docker-compose up -d
   
   # 访问 API 文档
   open http://localhost:8000/docs
   ```

3. **运行测试**
   ```bash
   pytest tests/test_logging.py -v
   pytest tests/test_api.py -v
   ```

### 兼容性

- Python >= 3.8
- Docker >= 20.10
- Docker Compose >= 2.0

### 贡献者

感谢所有为本次更新做出贡献的开发者！

---

## [0.1.0] - 初始版本

初始项目结构，包含算法、模型和数据结构的基础实现。
