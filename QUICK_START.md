# 快速入门指南

本指南将帮助您快速开始使用算法与模型 API 服务。

## 目录

- [前置要求](#前置要求)
- [安装](#安装)
- [快速开始](#快速开始)
- [使用示例](#使用示例)
- [下一步](#下一步)

## 前置要求

- Python >= 3.8
- Docker >= 20.10（可选，用于容器化部署）
- Docker Compose >= 2.0（可选）

## 安装

### 方式 1: 本地安装

```bash
# 克隆仓库
git clone <repository-url>
cd algo-models

# 安装依赖
pip install -r requirements.txt

# 安装项目包
pip install -e .
```

### 方式 2: Docker 安装

```bash
# 克隆仓库
git clone <repository-url>
cd algo-models

# 使用 docker-compose 启动
docker-compose up -d
```

## 快速开始

### 1. 启动 API 服务

**本地启动：**

```bash
./scripts/start_api.sh
```

或直接使用 uvicorn：

```bash
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
```

**Docker 启动：**

```bash
docker-compose up -d
```

### 2. 验证服务

访问 http://localhost:8000/health 检查服务状态：

```bash
curl http://localhost:8000/health
```

响应：
```json
{
  "status": "healthy",
  "version": "0.1.0"
}
```

### 3. 查看 API 文档

打开浏览器访问：

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 使用示例

### 1. 使用日志模块

```python
from src.logging import get_logger

# 获取 logger
logger = get_logger(__name__)

# 记录日志
logger.info("这是一条信息")
logger.warning("这是一条警告")
logger.error("这是一条错误")
```

运行示例：

```bash
python examples/logging_example.py
```

### 2. 调用排序 API

```bash
# 快速排序
curl -X POST "http://localhost:8000/api/v1/algorithms/sort" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [5, 2, 8, 1, 9],
    "algorithm": "quick_sort",
    "reverse": false
  }'
```

响应：
```json
{
  "sorted_data": [1, 2, 5, 8, 9],
  "algorithm": "quick_sort",
  "execution_time": 0.0001
}
```

### 3. 调用搜索 API

```bash
# 二分搜索
curl -X POST "http://localhost:8000/api/v1/algorithms/search" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [1, 2, 5, 8, 9],
    "target": 5,
    "algorithm": "binary_search"
  }'
```

### 4. 训练和预测模型

**训练线性回归模型：**

```bash
curl -X POST "http://localhost:8000/api/v1/models/train" \
  -H "Content-Type: application/json" \
  -d '{
    "model_type": "linear_regression",
    "X_train": [[1], [2], [3], [4], [5]],
    "y_train": [2, 4, 6, 8, 10]
  }'
```

**使用模型预测：**

```bash
curl -X POST "http://localhost:8000/api/v1/models/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "model_type": "linear_regression",
    "features": [[6], [7], [8]]
  }'
```

响应：
```json
{
  "predictions": [12.0, 14.0, 16.0],
  "model_type": "linear_regression",
  "execution_time": 0.0001
}
```

### 5. 使用 Python 客户端

```python
from examples.api_client_example import AlgoModelsClient

# 创建客户端
client = AlgoModelsClient("http://localhost:8000")

# 健康检查
health = client.health_check()
print(health)

# 排序
result = client.sort_array([5, 2, 8, 1, 9], algorithm="quick_sort")
print(result['sorted_data'])

# 训练模型
result = client.train_model(
    "linear_regression",
    [[1], [2], [3]],
    [2, 4, 6]
)
print(result)

# 预测
result = client.predict("linear_regression", [[4], [5]])
print(result['predictions'])
```

运行完整示例：

```bash
python examples/api_client_example.py
```

## 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_logging.py -v
pytest tests/test_api.py -v

# 查看测试覆盖率
pytest --cov=src tests/
```

## 查看日志

日志文件存储在 `logs/` 目录下：

```bash
# 查看主日志
tail -f logs/algo-models.log

# 查看 API 日志
tail -f logs/api.log
```

## Docker 常用命令

```bash
# 启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 查看服务状态
docker-compose ps

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 查看 API 容器日志
docker-compose logs -f api
```

## 停止服务

**本地服务：**

按 `Ctrl+C` 停止服务

**Docker 服务：**

```bash
docker-compose down
```

## 下一步

- 📖 阅读 [完整 API 文档](docs/API_USAGE.md)
- 📖 学习 [日志模块使用](docs/LOGGING.md)
- 📖 了解 [Docker 部署](docs/DOCKER_DEPLOYMENT.md)
- 🔍 浏览 [示例代码](examples/)
- 🧪 查看 [测试代码](tests/)

## 故障排查

### 端口已被占用

```bash
# 查看端口占用
lsof -i :8000

# 修改 docker-compose.yml 中的端口映射
ports:
  - "8001:8000"
```

### 无法连接到服务

```bash
# 检查服务是否运行
curl http://localhost:8000/health

# 查看日志
docker-compose logs api
tail -f logs/api.log
```

### Docker 构建失败

```bash
# 清理 Docker 缓存
docker system prune -a

# 重新构建
docker-compose build --no-cache
```

## 获取帮助

- 查看文档：[docs/](docs/)
- 提交问题：GitHub Issues
- 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件
