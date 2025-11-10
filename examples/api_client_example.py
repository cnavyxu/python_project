"""
API 客户端使用示例
"""

import requests
import json
from typing import List, Dict, Any


class AlgoModelsClient:
    """算法与模型 API 客户端"""

    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()

    def health_check(self) -> Dict[str, Any]:
        """健康检查"""
        response = self.session.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()

    def sort_array(
        self, data: List[float], algorithm: str = "quick_sort", reverse: bool = False
    ) -> Dict[str, Any]:
        """排序数组"""
        payload = {"data": data, "algorithm": algorithm, "reverse": reverse}

        response = self.session.post(
            f"{self.base_url}/api/v1/algorithms/sort", json=payload
        )
        response.raise_for_status()
        return response.json()

    def search_array(
        self, data: List[float], target: float, algorithm: str = "binary_search"
    ) -> Dict[str, Any]:
        """搜索数组"""
        payload = {"data": data, "target": target, "algorithm": algorithm}

        response = self.session.post(
            f"{self.base_url}/api/v1/algorithms/search", json=payload
        )
        response.raise_for_status()
        return response.json()

    def train_model(
        self,
        model_type: str,
        X_train: List[List[float]],
        y_train: List[float],
        model_params: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """训练模型"""
        payload = {
            "model_type": model_type,
            "X_train": X_train,
            "y_train": y_train,
            "model_params": model_params,
        }

        response = self.session.post(
            f"{self.base_url}/api/v1/models/train", json=payload
        )
        response.raise_for_status()
        return response.json()

    def predict(
        self, model_type: str, features: List[List[float]]
    ) -> Dict[str, Any]:
        """预测"""
        payload = {"model_type": model_type, "features": features}

        response = self.session.post(
            f"{self.base_url}/api/v1/models/predict", json=payload
        )
        response.raise_for_status()
        return response.json()

    def list_models(self) -> Dict[str, Any]:
        """列出可用模型"""
        response = self.session.get(f"{self.base_url}/api/v1/models/models")
        response.raise_for_status()
        return response.json()


def demo_sorting():
    """排序演示"""
    print("=== 排序演示 ===")

    client = AlgoModelsClient()

    # 快速排序
    data = [5, 2, 8, 1, 9, 3]
    print(f"原始数组: {data}")

    result = client.sort_array(data, algorithm="quick_sort", reverse=False)
    print(f"快速排序（升序）: {result['sorted_data']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")

    # 冒泡排序（降序）
    result = client.sort_array(data, algorithm="bubble_sort", reverse=True)
    print(f"冒泡排序（降序）: {result['sorted_data']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")


def demo_searching():
    """搜索演示"""
    print("\n=== 搜索演示 ===")

    client = AlgoModelsClient()

    # 二分搜索（需要有序数组）
    data = [1, 2, 3, 5, 8, 9]
    target = 5
    print(f"有序数组: {data}")
    print(f"搜索目标: {target}")

    result = client.search_array(data, target, algorithm="binary_search")
    print(f"二分搜索结果: 索引 {result['index']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")

    # 线性搜索
    data = [5, 2, 8, 1, 9, 3]
    target = 8
    print(f"\n无序数组: {data}")
    print(f"搜索目标: {target}")

    result = client.search_array(data, target, algorithm="linear_search")
    print(f"线性搜索结果: 索引 {result['index']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")


def demo_linear_regression():
    """线性回归演示"""
    print("\n=== 线性回归演示 ===")

    client = AlgoModelsClient()

    # 训练数据：y = 2x
    X_train = [[1], [2], [3], [4], [5]]
    y_train = [2, 4, 6, 8, 10]

    print(f"训练数据:")
    print(f"X: {X_train}")
    print(f"y: {y_train}")

    # 训练模型
    result = client.train_model("linear_regression", X_train, y_train)
    print(f"\n训练结果: {result['message']}")
    print(f"训练指标: {result['metrics']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")

    # 预测
    X_test = [[6], [7], [8]]
    print(f"\n测试数据: {X_test}")

    result = client.predict("linear_regression", X_test)
    print(f"预测结果: {result['predictions']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")


def demo_knn():
    """KNN 分类演示"""
    print("\n=== KNN 分类演示 ===")

    client = AlgoModelsClient()

    # 训练数据：两类点
    X_train = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]]
    y_train = [0, 0, 0, 1, 1, 1]

    print(f"训练数据:")
    print(f"X: {X_train}")
    print(f"y: {y_train}")

    # 训练模型
    result = client.train_model("knn", X_train, y_train, model_params={"k": 3})
    print(f"\n训练结果: {result['message']}")
    print(f"训练指标: {result['metrics']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")

    # 预测
    X_test = [[2, 2], [7, 7], [5, 5]]
    print(f"\n测试数据: {X_test}")

    result = client.predict("knn", X_test)
    print(f"预测结果: {result['predictions']}")
    print(f"执行时间: {result['execution_time']:.6f} 秒")


def demo_list_models():
    """列出模型演示"""
    print("\n=== 可用模型 ===")

    client = AlgoModelsClient()

    result = client.list_models()
    print(f"可用模型类型: {result['available_models']}")
    print(f"已训练模型: {result['trained_models']}")


def main():
    """主函数"""
    print("算法与模型 API 客户端示例\n")

    try:
        # 健康检查
        client = AlgoModelsClient()
        health = client.health_check()
        print(f"服务状态: {health['status']}")
        print(f"服务版本: {health['version']}\n")

        # 运行演示
        demo_sorting()
        demo_searching()
        demo_linear_regression()
        demo_knn()
        demo_list_models()

        print("\n所有演示完成！")

    except requests.exceptions.ConnectionError:
        print("错误: 无法连接到 API 服务")
        print("请确保服务正在运行: http://localhost:8000")
        print("启动命令: ./scripts/start_api.sh 或 docker-compose up")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}")
    except Exception as e:
        print(f"未知错误: {e}")


if __name__ == "__main__":
    main()
