"""
机器学习模型模块

实现各种经典机器学习算法
"""

import numpy as np
from typing import Optional


class LinearRegression:
    """线性回归模型"""
    
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights: Optional[np.ndarray] = None
        self.bias: float = 0
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        训练模型
        
        Args:
            X: 特征矩阵，形状为(n_samples, n_features)
            y: 目标值，形状为(n_samples,)
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            y_pred = np.dot(X, self.weights) + self.bias
            
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        预测
        
        Args:
            X: 特征矩阵
            
        Returns:
            预测值
        """
        return np.dot(X, self.weights) + self.bias


class LogisticRegression:
    """逻辑回归模型"""
    
    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights: Optional[np.ndarray] = None
        self.bias: float = 0
    
    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """训练模型"""
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            linear_pred = np.dot(X, self.weights) + self.bias
            y_pred = self._sigmoid(linear_pred)
            
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """预测类别"""
        linear_pred = np.dot(X, self.weights) + self.bias
        y_pred = self._sigmoid(linear_pred)
        return (y_pred >= threshold).astype(int)
    
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """预测概率"""
        linear_pred = np.dot(X, self.weights) + self.bias
        return self._sigmoid(linear_pred)


class KMeans:
    """K均值聚类"""
    
    def __init__(self, n_clusters: int = 3, max_iterations: int = 100):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations
        self.centroids: Optional[np.ndarray] = None
    
    def fit(self, X: np.ndarray):
        """训练模型"""
        n_samples = X.shape[0]
        random_indices = np.random.choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[random_indices]
        
        for _ in range(self.max_iterations):
            labels = self._assign_clusters(X)
            new_centroids = self._update_centroids(X, labels)
            
            if np.allclose(self.centroids, new_centroids):
                break
            
            self.centroids = new_centroids
    
    def _assign_clusters(self, X: np.ndarray) -> np.ndarray:
        """分配样本到最近的聚类中心"""
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)
    
    def _update_centroids(self, X: np.ndarray, labels: np.ndarray) -> np.ndarray:
        """更新聚类中心"""
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            cluster_points = X[labels == k]
            if len(cluster_points) > 0:
                centroids[k] = cluster_points.mean(axis=0)
        return centroids
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """预测聚类标签"""
        return self._assign_clusters(X)


__all__ = [
    "LinearRegression",
    "LogisticRegression",
    "KMeans",
]
