# API 使用文档

## 概述

本项目提供了基于 FastAPI 的 REST API 服务，用于访问算法和机器学习模型功能。

## 启动服务

### 本地启动

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
./scripts/start_api.sh

# 或直接使用 uvicorn
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
```

### Docker 启动

```bash
# 使用 docker-compose（推荐）
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 或手动构建和运行
./scripts/docker_build.sh
docker run -d -p 8000:8000 --name algo-models-api algo-models:latest
```

## API 端点

服务启动后，可以访问以下端点：

- **API 文档**: http://localhost:8000/docs
- **ReDoc 文档**: http://localhost:8000/redoc
- **健康检查**: http://localhost:8000/health

## 使用示例

### 1. 健康检查

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

### 2. 排序算法

#### 快速排序

```bash
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

#### 冒泡排序（降序）

```bash
curl -X POST "http://localhost:8000/api/v1/algorithms/sort" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [5, 2, 8, 1, 9],
    "algorithm": "bubble_sort",
    "reverse": true
  }'
```

### 3. 搜索算法

#### 二分搜索

```bash
curl -X POST "http://localhost:8000/api/v1/algorithms/search" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [1, 2, 5, 8, 9],
    "target": 5,
    "algorithm": "binary_search"
  }'
```

响应：
```json
{
  "index": 2,
  "algorithm": "binary_search",
  "execution_time": 0.0001
}
```

#### 线性搜索

```bash
curl -X POST "http://localhost:8000/api/v1/algorithms/search" \
  -H "Content-Type: application/json" \
  -d '{
    "data": [5, 2, 8, 1, 9],
    "target": 8,
    "algorithm": "linear_search"
  }'
```

### 4. 机器学习模型

#### 训练线性回归模型

```bash
curl -X POST "http://localhost:8000/api/v1/models/train" \
  -H "Content-Type: application/json" \
  -d '{
    "model_type": "linear_regression",
    "X_train": [[1], [2], [3], [4], [5]],
    "y_train": [2, 4, 6, 8, 10]
  }'
```

响应：
```json
{
  "message": "模型训练成功",
  "model_type": "linear_regression",
  "execution_time": 0.001,
  "metrics": {
    "mse": 0.0
  }
}
```

#### 使用模型预测

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

#### 训练 KNN 模型

```bash
curl -X POST "http://localhost:8000/api/v1/models/train" \
  -H "Content-Type: application/json" \
  -d '{
    "model_type": "knn",
    "X_train": [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]],
    "y_train": [0, 0, 0, 1, 1, 1],
    "model_params": {"k": 3}
  }'
```

### 5. 查询可用算法和模型

#### 列出排序算法

```bash
curl http://localhost:8000/api/v1/algorithms/algorithms/sort
```

#### 列出搜索算法

```bash
curl http://localhost:8000/api/v1/algorithms/algorithms/search
```

#### 列出可用模型

```bash
curl http://localhost:8000/api/v1/models/models
```

## Python 客户端示例

```python
import requests

BASE_URL = "http://localhost:8000"

# 排序
response = requests.post(
    f"{BASE_URL}/api/v1/algorithms/sort",
    json={
        "data": [5, 2, 8, 1, 9],
        "algorithm": "quick_sort",
        "reverse": False
    }
)
print(response.json())

# 训练模型
response = requests.post(
    f"{BASE_URL}/api/v1/models/train",
    json={
        "model_type": "linear_regression",
        "X_train": [[1], [2], [3], [4], [5]],
        "y_train": [2, 4, 6, 8, 10]
    }
)
print(response.json())

# 预测
response = requests.post(
    f"{BASE_URL}/api/v1/models/predict",
    json={
        "model_type": "linear_regression",
        "features": [[6], [7]]
    }
)
print(response.json())
```

## 环境变量配置

可以通过环境变量配置服务：

- `LOG_LEVEL`: 日志级别（DEBUG, INFO, WARNING, ERROR），默认 INFO
- `PYTHONPATH`: Python 模块搜索路径

## 日志

日志文件存储在 `logs/` 目录下：

- `algo-models.log`: 主日志文件
- `api.log`: API 服务日志

## 注意事项

1. 二分搜索要求输入数组已排序
2. 模型训练后存储在内存中，重启服务会丢失
3. 生产环境建议配置持久化存储和模型保存功能
4. 建议使用反向代理（如 Nginx）处理 HTTPS 和负载均衡
