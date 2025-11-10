# 贡献指南

感谢您对本项目的关注！我们欢迎各种形式的贡献。

## 如何贡献

### 报告Bug

如果您发现了bug，请创建一个issue，并包含以下信息：

- Bug的详细描述
- 复现步骤
- 预期行为
- 实际行为
- 系统环境（操作系统、Python版本等）

### 提出新功能

如果您有新功能的想法，请先创建一个issue讨论，包含：

- 功能描述
- 使用场景
- 可能的实现方案

### 提交代码

1. **Fork项目**

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **编写代码**
   - 遵循现有的代码风格
   - 为新功能添加测试
   - 更新相关文档

4. **运行测试**
   ```bash
   pytest
   ```

5. **代码格式化**
   ```bash
   black src tests
   isort src tests
   ```

6. **提交代码**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

7. **推送到您的fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **创建Pull Request**

## 代码规范

### Python代码风格

- 使用 Black 进行代码格式化（行长度：100）
- 使用 isort 进行导入排序
- 遵循 PEP 8 规范
- 使用类型注解

### 提交信息规范

使用语义化的提交信息：

- `feat:` 新功能
- `fix:` Bug修复
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

示例：
```
feat: add quick sort algorithm
fix: correct binary search edge case
docs: update README installation guide
```

### 测试

- 为新功能编写单元测试
- 确保所有测试通过
- 保持测试覆盖率在80%以上

### 文档

- 为公共API添加docstring
- 更新相关的教程和README
- 提供使用示例

## 开发环境设置

1. **克隆项目**
   ```bash
   git clone https://github.com/yourusername/algo-models.git
   cd algo-models
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

4. **设置pre-commit钩子**
   ```bash
   pre-commit install
   ```

## 问题反馈

如果您有任何问题，可以通过以下方式联系我们：

- 创建GitHub Issue
- 发送邮件到：your.email@example.com

再次感谢您的贡献！
