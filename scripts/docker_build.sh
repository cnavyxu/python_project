#!/bin/bash
# Docker 镜像构建脚本

set -e

echo "构建 Docker 镜像..."

# 镜像名称和标签
IMAGE_NAME="algo-models"
IMAGE_TAG=${1:-latest}

# 构建镜像
docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

echo "镜像构建完成: ${IMAGE_NAME}:${IMAGE_TAG}"
echo ""
echo "运行容器:"
echo "  docker run -d -p 8000:8000 --name algo-models-api ${IMAGE_NAME}:${IMAGE_TAG}"
echo ""
echo "或使用 docker-compose:"
echo "  docker-compose up -d"
