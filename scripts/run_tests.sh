#!/bin/bash

echo "运行测试..."
pytest tests/ -v --cov=src --cov-report=term-missing --cov-report=html

echo ""
echo "测试完成！覆盖率报告已生成在 htmlcov/ 目录"
