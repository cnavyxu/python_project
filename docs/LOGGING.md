# 日志模块使用文档

## 概述

日志模块提供了统一的日志配置和管理功能，支持控制台和文件输出、日志轮转等特性。

## 基本使用

### 快速开始

```python
from src.logging import get_logger

# 获取 logger
logger = get_logger()

# 记录不同级别的日志
logger.debug("调试信息")
logger.info("普通信息")
logger.warning("警告信息")
logger.error("错误信息")
logger.critical("严重错误")
```

### 为模块创建专用 Logger

```python
from src.logging import get_logger

# 为当前模块创建 logger
logger = get_logger(__name__)

logger.info("这是来自特定模块的日志")
```

## 高级配置

### 使用 LogConfig 自定义配置

```python
from src.logging import setup_logging, LogConfig

# 创建自定义配置
config = LogConfig(
    name="my_module",
    level="DEBUG",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    date_format="%Y-%m-%d %H:%M:%S",
    log_dir="logs",
    log_file="my_module.log",
    console_output=True,
    file_output=True,
    max_bytes=10 * 1024 * 1024,  # 10MB
    backup_count=5,
    rotation_type="size"  # 或 "time"
)

# 应用配置
logger = setup_logging(config)
```

### 日志轮转

#### 按大小轮转

```python
from src.logging import LogConfig, setup_logging

config = LogConfig(
    name="size_rotation",
    rotation_type="size",
    max_bytes=10 * 1024 * 1024,  # 10MB
    backup_count=5  # 保留 5 个备份
)

logger = setup_logging(config)
```

这将创建以下文件：
- `logs/size_rotation.log`
- `logs/size_rotation.log.1`
- `logs/size_rotation.log.2`
- ...

#### 按时间轮转

```python
from src.logging import LogConfig, setup_logging

config = LogConfig(
    name="time_rotation",
    rotation_type="time",
    backup_count=7  # 保留 7 天
)

logger = setup_logging(config)
```

每天午夜自动创建新的日志文件。

## 日志级别

| 级别 | 数值 | 用途 |
|------|------|------|
| DEBUG | 10 | 详细的调试信息 |
| INFO | 20 | 一般的信息性消息 |
| WARNING | 30 | 警告消息 |
| ERROR | 40 | 错误消息 |
| CRITICAL | 50 | 严重错误消息 |

## 日志格式

### 默认格式

```
%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

输出示例：
```
2024-01-10 10:30:45 - algo-models - INFO - 服务启动成功
```

### 自定义格式

```python
from src.logging import LogConfig, setup_logging

config = LogConfig(
    format="[%(levelname)s] %(asctime)s | %(name)s | %(funcName)s:%(lineno)d | %(message)s",
    date_format="%Y-%m-%d %H:%M:%S"
)

logger = setup_logging(config)
```

可用的格式化字段：
- `%(name)s`: Logger 名称
- `%(levelname)s`: 日志级别
- `%(asctime)s`: 时间戳
- `%(message)s`: 日志消息
- `%(filename)s`: 文件名
- `%(funcName)s`: 函数名
- `%(lineno)d`: 行号
- `%(pathname)s`: 完整路径
- `%(process)d`: 进程 ID
- `%(thread)d`: 线程 ID

## 实际应用示例

### 1. 算法模块日志

```python
from src.logging import get_logger
from src.utils import timer

logger = get_logger("algorithms.sorting")

@timer
def quick_sort(arr):
    logger.debug(f"开始排序，数组长度: {len(arr)}")
    
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    logger.debug(f"分区完成，左: {len(left)}, 中: {len(middle)}, 右: {len(right)}")
    
    return quick_sort(left) + middle + quick_sort(right)

result = quick_sort([3, 6, 8, 10, 1, 2, 1])
logger.info(f"排序完成: {result}")
```

### 2. 模型训练日志

```python
from src.logging import get_logger
import numpy as np

logger = get_logger("models.training")

class LinearRegression:
    def __init__(self):
        self.weights = None
        self.bias = None
        self.logger = get_logger("models.linear_regression")
    
    def fit(self, X, y, epochs=100):
        self.logger.info(f"开始训练，样本数: {len(X)}, 特征数: {X.shape[1]}")
        
        for epoch in range(epochs):
            # 训练逻辑
            loss = self._compute_loss(X, y)
            
            if epoch % 10 == 0:
                self.logger.debug(f"Epoch {epoch}/{epochs}, Loss: {loss:.4f}")
        
        self.logger.info("训练完成")
    
    def _compute_loss(self, X, y):
        # 损失计算
        return 0.0
```

### 3. API 请求日志

```python
from src.logging import get_logger
from fastapi import Request
import time

logger = get_logger("api.middleware")

async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    logger.info(f"请求开始: {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    logger.info(
        f"请求完成: {request.method} {request.url.path} "
        f"状态码: {response.status_code} 耗时: {process_time:.4f}s"
    )
    
    return response
```

### 4. 异常日志

```python
from src.logging import get_logger

logger = get_logger("error_handler")

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"计算结果: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logger.error(f"除零错误: {a} / {b}", exc_info=True)
        raise
    except Exception as e:
        logger.critical(f"未预期的错误: {str(e)}", exc_info=True)
        raise
```

## 配置文件示例

可以将日志配置放在 `config.yaml` 中：

```yaml
logging:
  name: "algo-models"
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  date_format: "%Y-%m-%d %H:%M:%S"
  log_dir: "logs"
  log_file: "app.log"
  console_output: true
  file_output: true
  max_bytes: 10485760  # 10MB
  backup_count: 5
  rotation_type: "size"
```

然后在代码中加载：

```python
import yaml
from src.logging import setup_logging, LogConfig

with open("config.yaml") as f:
    config_dict = yaml.safe_load(f)

config = LogConfig(**config_dict["logging"])
logger = setup_logging(config)
```

## 最佳实践

1. **为每个模块创建独立的 Logger**
   ```python
   logger = get_logger(__name__)
   ```

2. **使用合适的日志级别**
   - DEBUG: 开发和调试
   - INFO: 重要的业务逻辑
   - WARNING: 可能的问题
   - ERROR: 错误但程序可以继续
   - CRITICAL: 严重错误，程序可能无法继续

3. **记录异常堆栈**
   ```python
   try:
       # 代码
   except Exception as e:
       logger.error("错误信息", exc_info=True)
   ```

4. **避免在循环中记录过多日志**
   ```python
   # 不好
   for i in range(10000):
       logger.info(f"处理 {i}")
   
   # 好
   logger.info(f"开始处理 10000 条数据")
   for i in range(10000):
       if i % 1000 == 0:
           logger.debug(f"进度: {i/10000*100:.1f}%")
   logger.info("处理完成")
   ```

5. **敏感信息脱敏**
   ```python
   # 不要记录密码、token 等敏感信息
   logger.info(f"用户登录: {username}")  # 好
   # logger.info(f"密码: {password}")  # 不好
   ```

## 生产环境配置建议

1. **日志级别**: 使用 INFO 或 WARNING
2. **文件轮转**: 按大小或时间轮转，避免日志文件过大
3. **日志保留**: 根据存储空间和合规要求设置备份数量
4. **集中式日志**: 考虑使用 ELK、Loki 等日志收集系统
5. **监控告警**: 对 ERROR 和 CRITICAL 级别日志设置告警

## 性能考虑

1. 日志操作是 I/O 密集型，避免过度使用
2. 使用异步日志处理器（如 QueueHandler）提高性能
3. 在性能关键代码路径中使用 DEBUG 级别，生产环境关闭 DEBUG
4. 考虑使用结构化日志（JSON 格式）便于解析和分析
