# 算法与模型库

这是一个专注于算法和机器学习模型实现的Python项目。

## 项目结构

```
.
├── src/                        # 源代码目录
│   ├── algorithms/             # 算法实现
│   │   ├── sorting/            # 排序算法
│   │   ├── searching/          # 搜索算法
│   │   ├── graph/              # 图算法
│   │   ├── dynamic_programming/# 动态规划
│   │   ├── greedy/             # 贪心算法
│   │   └── backtracking/       # 回溯算法
│   ├── models/                 # 模型实现
│   │   ├── ml/                 # 机器学习模型
│   │   ├── dl/                 # 深度学习模型
│   │   └── statistical/        # 统计模型
│   ├── data_structures/        # 数据结构实现
│   ├── utils/                  # 工具函数
│   ├── config/                 # 配置文件
│   ├── logging/                # 日志模块
│   └── api/                    # API 服务模块
├── tests/                      # 测试代码
│   ├── test_algorithms/        # 算法测试
│   ├── test_models/            # 模型测试
│   └── test_data_structures/   # 数据结构测试
├── examples/                   # 示例代码
├── notebooks/                  # Jupyter notebooks
├── docs/                       # 文档
│   ├── api/                    # API文档
│   └── tutorials/              # 教程
├── data/                       # 数据文件
│   ├── raw/                    # 原始数据
│   ├── processed/              # 处理后的数据
│   └── samples/                # 示例数据
├── scripts/                    # 脚本文件
└── benchmarks/                 # 性能基准测试
```

## 安装

### 基础安装

```bash
pip install -r requirements.txt
```

### 开发安装

```bash
pip install -r requirements-dev.txt
pip install -e .
```

## 使用示例

### 算法示例

```python
from src.algorithms.sorting import quick_sort
from src.algorithms.searching import binary_search

# 排序示例
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)

# 搜索示例
index = binary_search(sorted_arr, 25)
```

### 模型示例

```python
from src.models.ml import LinearRegression
from src.data_structures import Dataset

# 创建模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测
predictions = model.predict(X_test)
```

## API 服务

本项目提供了基于 FastAPI 的 REST API 服务，可以通过 HTTP 接口访问算法和模型功能。

### 启动 API 服务

**本地启动：**

```bash
# 使用启动脚本
./scripts/start_api.sh

# 或直接使用 uvicorn
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
```

**Docker 启动：**

```bash
# 使用 docker-compose（推荐）
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

### API 文档

服务启动后，访问以下地址：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- 健康检查: http://localhost:8000/health

详细 API 使用说明请参考 [docs/API_USAGE.md](docs/API_USAGE.md)

## 日志模块

项目提供了统一的日志管理功能，支持控制台和文件输出、日志轮转等特性。

```python
from src.logging import get_logger

logger = get_logger(__name__)
logger.info("这是一条日志信息")
```

详细使用说明请参考 [docs/LOGGING.md](docs/LOGGING.md)

## Docker 部署

项目支持使用 Docker 进行部署：

```bash
# 构建镜像
docker build -t algo-models:latest .

# 运行容器
docker run -d -p 8000:8000 --name algo-models-api algo-models:latest

# 或使用 docker-compose
docker-compose up -d
```

详细部署说明请参考 [docs/DOCKER_DEPLOYMENT.md](docs/DOCKER_DEPLOYMENT.md)

## 测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_algorithms/
pytest tests/test_api.py
pytest tests/test_logging.py

# 查看覆盖率
pytest --cov=src tests/
```

## 文档

完整文档请查看 [docs/](docs/) 目录：

- [API 使用文档](docs/API_USAGE.md)
- [日志模块文档](docs/LOGGING.md)
- [Docker 部署文档](docs/DOCKER_DEPLOYMENT.md)

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 许可证

MIT License
