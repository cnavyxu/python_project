# 项目结构说明

这是一个完整的 Python 算法与模型库项目结构。

## 完整目录树

```
.
├── .git/                       # Git版本控制目录
├── .gitignore                  # Git忽略文件配置
├── .pre-commit-config.yaml     # Pre-commit钩子配置
├── README.md                   # 项目说明文档
├── LICENSE                     # 开源许可证
├── CONTRIBUTING.md             # 贡献指南
├── PROJECT_STRUCTURE.md        # 本文件
│
├── setup.py                    # 项目安装配置（传统方式）
├── pyproject.toml             # 现代Python项目配置
├── requirements.txt            # 核心依赖
├── requirements-dev.txt        # 开发依赖
├── config.example.yaml         # 配置文件示例
│
├── src/                        # 源代码目录
│   ├── __init__.py
│   │
│   ├── algorithms/             # 算法实现
│   │   ├── __init__.py
│   │   ├── sorting/            # 排序算法（快速排序、归并排序、冒泡排序）
│   │   ├── searching/          # 搜索算法（二分搜索、线性搜索、跳跃搜索）
│   │   ├── graph/              # 图算法（BFS、DFS、Dijkstra）
│   │   ├── dynamic_programming/# 动态规划（斐波那契、背包、最长公共子序列）
│   │   ├── greedy/             # 贪心算法（活动选择、分数背包、哈夫曼编码）
│   │   └── backtracking/       # 回溯算法（N皇后、数独、全排列、组合）
│   │
│   ├── models/                 # 模型实现
│   │   ├── __init__.py
│   │   ├── ml/                 # 机器学习（线性回归、逻辑回归、K均值）
│   │   ├── dl/                 # 深度学习（神经网络层、激活函数）
│   │   └── statistical/        # 统计模型（朴素贝叶斯、LDA、PCA）
│   │
│   ├── data_structures/        # 数据结构实现
│   │   └── __init__.py         # 链表、树、栈、队列、堆
│   │
│   ├── utils/                  # 工具函数
│   │   └── __init__.py         # 计时器、记忆化、数据处理、评估指标
│   │
│   └── config/                 # 配置管理
│       └── __init__.py         # 配置类实现
│
├── tests/                      # 测试代码
│   ├── __init__.py
│   ├── test_algorithms/        # 算法测试
│   │   ├── __init__.py
│   │   ├── test_sorting.py
│   │   └── test_searching.py
│   ├── test_models/            # 模型测试
│   │   └── __init__.py
│   └── test_data_structures/   # 数据结构测试
│       ├── __init__.py
│       └── test_basic.py
│
├── examples/                   # 示例代码
│   ├── sorting_example.py      # 排序算法演示
│   └── ml_example.py           # 机器学习演示
│
├── notebooks/                  # Jupyter notebooks
│   └── README.md               # Notebooks说明
│
├── docs/                       # 文档
│   ├── README.md               # 文档索引
│   ├── api/                    # API文档目录
│   └── tutorials/              # 教程目录
│       ├── algorithms.md       # 算法教程
│       ├── models.md           # 模型教程
│       └── data_structures.md  # 数据结构教程
│
├── data/                       # 数据文件
│   ├── README.md
│   ├── raw/                    # 原始数据
│   ├── processed/              # 处理后的数据
│   └── samples/                # 示例数据
│       └── sample_data.py      # 生成示例数据的工具
│
├── scripts/                    # 脚本文件
│   ├── run_tests.sh            # 测试运行脚本
│   └── format_code.sh          # 代码格式化脚本
│
├── benchmarks/                 # 性能基准测试
│   └── sorting_benchmark.py    # 排序算法性能测试
│
└── venv/                       # 虚拟环境（不提交到Git）

```

## 主要模块说明

### 1. 算法模块 (src/algorithms/)

包含各种经典算法的实现：

- **排序算法**: 快速排序、归并排序、冒泡排序
- **搜索算法**: 二分搜索、线性搜索、跳跃搜索
- **图算法**: 广度优先搜索、深度优先搜索、Dijkstra最短路径
- **动态规划**: 斐波那契数列、0-1背包、最长公共子序列、零钱兑换
- **贪心算法**: 活动选择、分数背包、哈夫曼编码
- **回溯算法**: N皇后、数独求解、全排列、组合

### 2. 模型模块 (src/models/)

包含机器学习和深度学习模型：

- **机器学习**: 线性回归、逻辑回归、K均值聚类
- **深度学习**: 全连接层、ReLU激活、Sigmoid激活、简单神经网络
- **统计模型**: 高斯朴素贝叶斯、线性判别分析、主成分分析

### 3. 数据结构模块 (src/data_structures/)

包含常用数据结构：

- **链表**: 单向链表
- **树**: 二叉搜索树
- **栈**: 后进先出数据结构
- **队列**: 先进先出数据结构
- **堆**: 最小堆

### 4. 工具模块 (src/utils/)

提供各种辅助功能：

- **装饰器**: 计时器、记忆化
- **数据处理**: 数据划分、标准化、缩放
- **评估指标**: 准确率、均方误差、R²分数

### 5. 配置模块 (src/config/)

提供配置管理功能，支持从YAML文件加载配置。

## 使用指南

### 快速开始

```bash
# 1. 克隆项目
git clone <repository-url>
cd <project-name>

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行示例
python examples/sorting_example.py
python examples/ml_example.py
```

### 开发环境设置

```bash
# 安装开发依赖
pip install -r requirements-dev.txt

# 安装包（可编辑模式）
pip install -e .

# 设置pre-commit钩子
pre-commit install
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_algorithms/

# 查看覆盖率
pytest --cov=src tests/
```

### 代码格式化

```bash
# 使用脚本
./scripts/format_code.sh

# 或手动运行
isort src tests examples
black src tests examples
```

### 性能基准测试

```bash
python benchmarks/sorting_benchmark.py
```

## 扩展建议

### 添加新算法

1. 在 `src/algorithms/` 相应子目录中添加实现
2. 在 `tests/test_algorithms/` 中添加测试
3. 在 `docs/tutorials/algorithms.md` 中添加文档
4. 在 `examples/` 中添加使用示例

### 添加新模型

1. 在 `src/models/` 相应子目录中添加实现
2. 在 `tests/test_models/` 中添加测试
3. 在 `docs/tutorials/models.md` 中添加文档
4. 在 `examples/` 中添加使用示例

### 添加新数据结构

1. 在 `src/data_structures/__init__.py` 中添加实现
2. 在 `tests/test_data_structures/` 中添加测试
3. 在 `docs/tutorials/data_structures.md` 中添加文档

## 注意事项

- 所有代码都应遵循PEP 8规范
- 新功能必须包含测试
- 保持测试覆盖率在80%以上
- 为公共API提供详细的docstring
- 提交前运行代码格式化工具
- 使用语义化的提交信息

## 技术栈

- **Python**: 3.8+
- **核心依赖**: NumPy, SciPy, Pandas, scikit-learn
- **可视化**: Matplotlib, Seaborn
- **测试**: pytest, pytest-cov
- **代码质量**: Black, isort, flake8, mypy
- **文档**: Sphinx

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件
