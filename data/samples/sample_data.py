"""
生成示例数据的工具函数
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np


def generate_linear_regression_data(n_samples=100, n_features=1, noise=0.1, random_state=42):
    """
    生成线性回归数据
    
    Args:
        n_samples: 样本数量
        n_features: 特征数量
        noise: 噪声水平
        random_state: 随机种子
        
    Returns:
        X, y: 特征矩阵和目标值
    """
    np.random.seed(random_state)
    X = np.random.randn(n_samples, n_features)
    true_weights = np.random.randn(n_features)
    y = X.dot(true_weights) + np.random.randn(n_samples) * noise
    return X, y


def generate_classification_data(n_samples=200, n_features=2, n_classes=2, random_state=42):
    """
    生成分类数据
    
    Args:
        n_samples: 样本数量
        n_features: 特征数量
        n_classes: 类别数量
        random_state: 随机种子
        
    Returns:
        X, y: 特征矩阵和标签
    """
    np.random.seed(random_state)
    samples_per_class = n_samples // n_classes
    
    X = []
    y = []
    
    for i in range(n_classes):
        center = np.random.randn(n_features) * 3
        samples = np.random.randn(samples_per_class, n_features) + center
        X.append(samples)
        y.append(np.full(samples_per_class, i))
    
    X = np.vstack(X)
    y = np.concatenate(y)
    
    indices = np.random.permutation(n_samples)
    X = X[indices]
    y = y[indices]
    
    return X, y


def generate_clustering_data(n_samples=150, n_features=2, n_clusters=3, random_state=42):
    """
    生成聚类数据
    
    Args:
        n_samples: 样本数量
        n_features: 特征数量
        n_clusters: 聚类中心数量
        random_state: 随机种子
        
    Returns:
        X: 特征矩阵
    """
    np.random.seed(random_state)
    samples_per_cluster = n_samples // n_clusters
    
    X = []
    
    for i in range(n_clusters):
        center = np.random.randn(n_features) * 5
        samples = np.random.randn(samples_per_cluster, n_features) + center
        X.append(samples)
    
    X = np.vstack(X)
    
    indices = np.random.permutation(n_samples)
    X = X[indices]
    
    return X


if __name__ == "__main__":
    print("生成示例数据...")
    
    X_reg, y_reg = generate_linear_regression_data()
    print(f"线性回归数据: X.shape={X_reg.shape}, y.shape={y_reg.shape}")
    
    X_clf, y_clf = generate_classification_data()
    print(f"分类数据: X.shape={X_clf.shape}, y.shape={y_clf.shape}")
    
    X_cluster = generate_clustering_data()
    print(f"聚类数据: X.shape={X_cluster.shape}")
    
    print("\n示例数据生成完成！")
