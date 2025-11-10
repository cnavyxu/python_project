#!/bin/bash

echo "格式化代码..."

echo "1. 运行 isort..."
isort src tests examples

echo "2. 运行 black..."
black src tests examples

echo ""
echo "代码格式化完成！"
