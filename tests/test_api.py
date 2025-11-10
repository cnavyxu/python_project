"""
API 服务测试
"""

import pytest
from fastapi.testclient import TestClient

from src.api.app import app

client = TestClient(app)


def test_health_check():
    """测试健康检查端点"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_root_endpoint():
    """测试根路径端点"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"


def test_sort_quick_sort():
    """测试快速排序"""
    response = client.post(
        "/api/v1/algorithms/sort",
        json={"data": [5, 2, 8, 1, 9], "algorithm": "quick_sort", "reverse": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sorted_data"] == [1, 2, 5, 8, 9]
    assert data["algorithm"] == "quick_sort"
    assert "execution_time" in data


def test_sort_bubble_sort():
    """测试冒泡排序"""
    response = client.post(
        "/api/v1/algorithms/sort",
        json={"data": [5, 2, 8, 1, 9], "algorithm": "bubble_sort", "reverse": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sorted_data"] == [1, 2, 5, 8, 9]


def test_sort_reverse():
    """测试降序排序"""
    response = client.post(
        "/api/v1/algorithms/sort",
        json={"data": [5, 2, 8, 1, 9], "algorithm": "quick_sort", "reverse": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["sorted_data"] == [9, 8, 5, 2, 1]


def test_sort_invalid_algorithm():
    """测试无效排序算法"""
    response = client.post(
        "/api/v1/algorithms/sort",
        json={"data": [5, 2, 8], "algorithm": "invalid_sort", "reverse": False},
    )
    assert response.status_code == 400


def test_binary_search():
    """测试二分搜索"""
    response = client.post(
        "/api/v1/algorithms/search",
        json={"data": [1, 2, 5, 8, 9], "target": 5, "algorithm": "binary_search"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["index"] == 2
    assert data["algorithm"] == "binary_search"


def test_linear_search():
    """测试线性搜索"""
    response = client.post(
        "/api/v1/algorithms/search",
        json={"data": [5, 2, 8, 1, 9], "target": 8, "algorithm": "linear_search"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["index"] == 2


def test_search_not_found():
    """测试搜索不到目标"""
    response = client.post(
        "/api/v1/algorithms/search",
        json={"data": [1, 2, 3], "target": 10, "algorithm": "linear_search"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["index"] == -1


def test_train_linear_regression():
    """测试训练线性回归模型"""
    response = client.post(
        "/api/v1/models/train",
        json={
            "model_type": "linear_regression",
            "X_train": [[1], [2], [3], [4], [5]],
            "y_train": [2, 4, 6, 8, 10],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "模型训练成功"
    assert data["model_type"] == "linear_regression"
    assert "metrics" in data
    assert "mse" in data["metrics"]


def test_train_knn():
    """测试训练 KNN 模型"""
    response = client.post(
        "/api/v1/models/train",
        json={
            "model_type": "knn",
            "X_train": [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]],
            "y_train": [0, 0, 0, 1, 1, 1],
            "model_params": {"k": 3},
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "模型训练成功"
    assert data["model_type"] == "knn"


def test_predict_linear_regression():
    """测试线性回归预测"""
    # 先训练
    client.post(
        "/api/v1/models/train",
        json={
            "model_type": "linear_regression",
            "X_train": [[1], [2], [3]],
            "y_train": [2, 4, 6],
        },
    )

    # 预测
    response = client.post(
        "/api/v1/models/predict",
        json={"model_type": "linear_regression", "features": [[4], [5]]},
    )
    assert response.status_code == 200
    data = response.json()
    assert "predictions" in data
    assert len(data["predictions"]) == 2


def test_predict_without_training():
    """测试未训练模型的预测"""
    response = client.post(
        "/api/v1/models/predict",
        json={"model_type": "untrained_model", "features": [[1], [2]]},
    )
    assert response.status_code == 400


def test_list_models():
    """测试列出可用模型"""
    response = client.get("/api/v1/models/models")
    assert response.status_code == 200
    data = response.json()
    assert "available_models" in data
    assert "trained_models" in data
    assert "linear_regression" in data["available_models"]
    assert "knn" in data["available_models"]


def test_list_sort_algorithms():
    """测试列出排序算法"""
    response = client.get("/api/v1/algorithms/algorithms/sort")
    assert response.status_code == 200
    data = response.json()
    assert "algorithms" in data
    assert "quick_sort" in data["algorithms"]
    assert "bubble_sort" in data["algorithms"]


def test_list_search_algorithms():
    """测试列出搜索算法"""
    response = client.get("/api/v1/algorithms/algorithms/search")
    assert response.status_code == 200
    data = response.json()
    assert "algorithms" in data
    assert "binary_search" in data["algorithms"]
    assert "linear_search" in data["algorithms"]


def test_api_documentation():
    """测试 API 文档可访问"""
    response = client.get("/docs")
    assert response.status_code == 200

    response = client.get("/redoc")
    assert response.status_code == 200
