"""
统计模型模块

实现各种统计模型和方法
"""

import numpy as np
from typing import Tuple, Optional


class GaussianNaiveBayes:
    """高斯朴素贝叶斯分类器"""
    
    def __init__(self):
        self.classes: Optional[np.ndarray] = None
        self.mean: Optional[np.ndarray] = None
        self.var: Optional[np.ndarray] = None
        self.priors: Optional[np.ndarray] = None
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """训练模型"""
        self.classes = np.unique(y)
        n_classes = len(self.classes)
        n_features = X.shape[1]
        
        self.mean = np.zeros((n_classes, n_features))
        self.var = np.zeros((n_classes, n_features))
        self.priors = np.zeros(n_classes)
        
        for idx, c in enumerate(self.classes):
            X_c = X[y == c]
            self.mean[idx] = X_c.mean(axis=0)
            self.var[idx] = X_c.var(axis=0)
            self.priors[idx] = X_c.shape[0] / X.shape[0]
    
    def _gaussian_probability(self, x: np.ndarray, mean: float, var: float) -> float:
        """计算高斯概率密度"""
        eps = 1e-4
        coefficient = 1 / np.sqrt(2 * np.pi * var + eps)
        exponent = np.exp(-((x - mean) ** 2) / (2 * var + eps))
        return coefficient * exponent
    
    def _predict_single(self, x: np.ndarray) -> int:
        """预测单个样本"""
        posteriors = []
        
        for idx, c in enumerate(self.classes):
            prior = np.log(self.priors[idx])
            posterior = np.sum(np.log(self._gaussian_probability(x, self.mean[idx], self.var[idx])))
            posterior += prior
            posteriors.append(posterior)
        
        return self.classes[np.argmax(posteriors)]
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """预测"""
        return np.array([self._predict_single(x) for x in X])


class LinearDiscriminantAnalysis:
    """线性判别分析"""
    
    def __init__(self, n_components: int = 2):
        self.n_components = n_components
        self.w: Optional[np.ndarray] = None
        self.mean: Optional[np.ndarray] = None
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """训练模型"""
        n_features = X.shape[1]
        class_labels = np.unique(y)
        
        mean_overall = np.mean(X, axis=0)
        S_W = np.zeros((n_features, n_features))
        S_B = np.zeros((n_features, n_features))
        
        for c in class_labels:
            X_c = X[y == c]
            mean_c = np.mean(X_c, axis=0)
            S_W += (X_c - mean_c).T.dot(X_c - mean_c)
            
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean_overall).reshape(n_features, 1)
            S_B += n_c * (mean_diff).dot(mean_diff.T)
        
        A = np.linalg.inv(S_W).dot(S_B)
        eigenvalues, eigenvectors = np.linalg.eig(A)
        
        eigenvectors = eigenvectors.T
        idxs = np.argsort(abs(eigenvalues))[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]
        
        self.w = eigenvectors[:self.n_components]
        self.mean = mean_overall
    
    def transform(self, X: np.ndarray) -> np.ndarray:
        """转换数据"""
        return np.dot(X - self.mean, self.w.T)


class PrincipalComponentAnalysis:
    """主成分分析"""
    
    def __init__(self, n_components: int = 2):
        self.n_components = n_components
        self.components: Optional[np.ndarray] = None
        self.mean: Optional[np.ndarray] = None
    
    def fit(self, X: np.ndarray):
        """训练模型"""
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        cov_matrix = np.cov(X_centered.T)
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        
        eigenvectors = eigenvectors.T
        idxs = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]
        
        self.components = eigenvectors[:self.n_components]
    
    def transform(self, X: np.ndarray) -> np.ndarray:
        """转换数据"""
        X_centered = X - self.mean
        return np.dot(X_centered, self.components.T)
    
    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """拟合并转换数据"""
        self.fit(X)
        return self.transform(X)


__all__ = [
    "GaussianNaiveBayes",
    "LinearDiscriminantAnalysis",
    "PrincipalComponentAnalysis",
]
