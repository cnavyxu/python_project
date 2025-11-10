"""
深度学习模型模块

实现各种深度学习模型和组件
"""

import numpy as np
from typing import List, Tuple, Optional


class Layer:
    """神经网络层的基类"""
    
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        raise NotImplementedError
    
    def backward(self, grad: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class DenseLayer(Layer):
    """全连接层"""
    
    def __init__(self, input_size: int, output_size: int, learning_rate: float = 0.01):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.bias = np.zeros((1, output_size))
        self.learning_rate = learning_rate
        self.inputs: Optional[np.ndarray] = None
    
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """前向传播"""
        self.inputs = inputs
        return np.dot(inputs, self.weights) + self.bias
    
    def backward(self, grad: np.ndarray) -> np.ndarray:
        """反向传播"""
        d_weights = np.dot(self.inputs.T, grad)
        d_bias = np.sum(grad, axis=0, keepdims=True)
        d_inputs = np.dot(grad, self.weights.T)
        
        self.weights -= self.learning_rate * d_weights
        self.bias -= self.learning_rate * d_bias
        
        return d_inputs


class ReLU(Layer):
    """ReLU激活函数"""
    
    def __init__(self):
        self.inputs: Optional[np.ndarray] = None
    
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        self.inputs = inputs
        return np.maximum(0, inputs)
    
    def backward(self, grad: np.ndarray) -> np.ndarray:
        return grad * (self.inputs > 0)


class Sigmoid(Layer):
    """Sigmoid激活函数"""
    
    def __init__(self):
        self.output: Optional[np.ndarray] = None
    
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        self.output = 1 / (1 + np.exp(-inputs))
        return self.output
    
    def backward(self, grad: np.ndarray) -> np.ndarray:
        return grad * self.output * (1 - self.output)


class NeuralNetwork:
    """简单的神经网络"""
    
    def __init__(self, layers: List[Layer]):
        self.layers = layers
    
    def forward(self, X: np.ndarray) -> np.ndarray:
        """前向传播"""
        output = X
        for layer in self.layers:
            output = layer.forward(output)
        return output
    
    def backward(self, grad: np.ndarray):
        """反向传播"""
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
    
    def train_step(self, X: np.ndarray, y: np.ndarray) -> float:
        """单步训练"""
        predictions = self.forward(X)
        loss = np.mean((predictions - y) ** 2)
        grad = 2 * (predictions - y) / y.shape[0]
        self.backward(grad)
        return loss
    
    def fit(self, X: np.ndarray, y: np.ndarray, epochs: int = 100, verbose: bool = True):
        """训练模型"""
        for epoch in range(epochs):
            loss = self.train_step(X, y)
            if verbose and (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """预测"""
        return self.forward(X)


__all__ = [
    "Layer",
    "DenseLayer",
    "ReLU",
    "Sigmoid",
    "NeuralNetwork",
]
