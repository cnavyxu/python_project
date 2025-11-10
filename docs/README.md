# 文档

本目录包含项目的详细文档。

## 目录结构

- `api/`: API参考文档
- `tutorials/`: 教程和指南

## 快速开始

请参考主目录的 [README.md](../README.md) 获取快速开始指南。

## 教程

- [算法教程](tutorials/algorithms.md)
- [模型教程](tutorials/models.md)
- [数据结构教程](tutorials/data_structures.md)

## API文档

详细的API文档可以通过以下方式生成：

```bash
cd docs
sphinx-build -b html . _build
```

生成的HTML文档将位于 `_build` 目录中。
