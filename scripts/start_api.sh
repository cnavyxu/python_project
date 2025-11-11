#!/bin/bash
# API 服务启动脚本

set -e

echo "启动算法与模型 API 服务..."

# 检查是否在虚拟环境中
if [ -z "$VIRTUAL_ENV" ]; then
    echo "警告: 未检测到虚拟环境，建议在虚拟环境中运行"
fi

# 设置 Python 路径
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# 创建日志目录
mkdir -p logs

# 启动 API 服务
echo "服务将在 http://0.0.0.0:8000 启动"
echo "API 文档: http://localhost:8000/docs"
echo "按 Ctrl+C 停止服务"

uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload
