"""
机器学习模型示例

演示如何使用机器学习模型
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from src.models.ml import LinearRegression, LogisticRegression, KMeans
from src.utils import train_test_split, accuracy_score, mean_squared_error


def demo_linear_regression():
    """线性回归演示"""
    print("线性回归演示")
    print("-" * 40)
    
    np.random.seed(42)
    X = np.random.randn(100, 1)
    y = 2 * X.squeeze() + 1 + np.random.randn(100) * 0.1
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression(learning_rate=0.01, n_iterations=1000)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"权重: {model.weights}")
    print(f"偏置: {model.bias}")
    print(f"测试集MSE: {mse:.4f}")


def demo_logistic_regression():
    """逻辑回归演示"""
    print("\n\n逻辑回归演示")
    print("-" * 40)
    
    np.random.seed(42)
    X = np.random.randn(200, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(learning_rate=0.1, n_iterations=1000)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"测试集准确率: {accuracy:.4f}")


def demo_kmeans():
    """K均值聚类演示"""
    print("\n\nK均值聚类演示")
    print("-" * 40)
    
    np.random.seed(42)
    X = np.vstack([
        np.random.randn(50, 2) + [2, 2],
        np.random.randn(50, 2) + [-2, -2],
        np.random.randn(50, 2) + [2, -2],
    ])
    
    model = KMeans(n_clusters=3, max_iterations=100)
    model.fit(X)
    
    labels = model.predict(X)
    print(f"聚类中心:\n{model.centroids}")
    print(f"前10个样本的标签: {labels[:10]}")


if __name__ == "__main__":
    print("=" * 50)
    print("机器学习模型演示")
    print("=" * 50)
    
    demo_linear_regression()
    demo_logistic_regression()
    demo_kmeans()
