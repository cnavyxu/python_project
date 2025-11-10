"""
工具函数模块

提供各种辅助工具函数
"""

import time
import functools
from typing import Callable, Any
import numpy as np


def timer(func: Callable) -> Callable:
    """
    计时装饰器
    
    用于测量函数执行时间
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper


def memoize(func: Callable) -> Callable:
    """
    记忆化装饰器
    
    缓存函数调用结果
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def train_test_split(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, random_state: int = None):
    """
    划分训练集和测试集
    
    Args:
        X: 特征矩阵
        y: 目标值
        test_size: 测试集比例
        random_state: 随机种子
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    n_samples = X.shape[0]
    n_test = int(n_samples * test_size)
    
    indices = np.random.permutation(n_samples)
    test_indices = indices[:n_test]
    train_indices = indices[n_test:]
    
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]


def normalize(X: np.ndarray) -> np.ndarray:
    """
    标准化数据（Z-score标准化）
    
    Args:
        X: 输入数据
        
    Returns:
        标准化后的数据
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / (std + 1e-8)


def min_max_scale(X: np.ndarray, feature_range: tuple = (0, 1)) -> np.ndarray:
    """
    最小-最大缩放
    
    Args:
        X: 输入数据
        feature_range: 缩放范围
        
    Returns:
        缩放后的数据
    """
    min_val, max_val = feature_range
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    
    X_scaled = (X - X_min) / (X_max - X_min + 1e-8)
    return X_scaled * (max_val - min_val) + min_val


def accuracy_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    计算准确率
    
    Args:
        y_true: 真实标签
        y_pred: 预测标签
        
    Returns:
        准确率
    """
    return np.mean(y_true == y_pred)


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    计算均方误差
    
    Args:
        y_true: 真实值
        y_pred: 预测值
        
    Returns:
        均方误差
    """
    return np.mean((y_true - y_pred) ** 2)


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    计算R²分数
    
    Args:
        y_true: 真实值
        y_pred: 预测值
        
    Returns:
        R²分数
    """
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / (ss_tot + 1e-8))


__all__ = [
    "timer",
    "memoize",
    "train_test_split",
    "normalize",
    "min_max_scale",
    "accuracy_score",
    "mean_squared_error",
    "r2_score",
]
