# 模型教程

本教程介绍如何使用项目中实现的各种机器学习和深度学习模型。

## 机器学习模型

### 线性回归

```python
import numpy as np
from src.models.ml import LinearRegression
from src.utils import train_test_split, mean_squared_error

# 生成数据
X = np.random.randn(100, 1)
y = 2 * X.squeeze() + 1 + np.random.randn(100) * 0.1

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 训练模型
model = LinearRegression(learning_rate=0.01, n_iterations=1000)
model.fit(X_train, y_train)

# 预测
predictions = model.predict(X_test)

# 评估
mse = mean_squared_error(y_test, predictions)
print(f"MSE: {mse}")
```

### 逻辑回归

```python
import numpy as np
from src.models.ml import LogisticRegression
from src.utils import train_test_split, accuracy_score

# 生成二分类数据
X = np.random.randn(200, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 训练模型
model = LogisticRegression(learning_rate=0.1, n_iterations=1000)
model.fit(X_train, y_train)

# 预测
predictions = model.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
```

### K均值聚类

```python
import numpy as np
from src.models.ml import KMeans

# 生成聚类数据
X = np.vstack([
    np.random.randn(50, 2) + [2, 2],
    np.random.randn(50, 2) + [-2, -2],
    np.random.randn(50, 2) + [2, -2],
])

# 训练模型
model = KMeans(n_clusters=3, max_iterations=100)
model.fit(X)

# 预测聚类标签
labels = model.predict(X)
print(f"Cluster centers:\n{model.centroids}")
```

## 深度学习模型

### 简单神经网络

```python
import numpy as np
from src.models.dl import NeuralNetwork, DenseLayer, ReLU, Sigmoid

# 创建网络
layers = [
    DenseLayer(2, 4, learning_rate=0.01),
    ReLU(),
    DenseLayer(4, 1, learning_rate=0.01),
    Sigmoid()
]

model = NeuralNetwork(layers)

# 生成数据
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(float).reshape(-1, 1)

# 训练模型
model.fit(X, y, epochs=100, verbose=True)

# 预测
predictions = model.predict(X)
```

## 统计模型

### 高斯朴素贝叶斯

```python
import numpy as np
from src.models.statistical import GaussianNaiveBayes
from src.utils import train_test_split, accuracy_score

# 生成数据
X = np.random.randn(200, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 训练模型
model = GaussianNaiveBayes()
model.fit(X_train, y_train)

# 预测
predictions = model.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
```

### 主成分分析 (PCA)

```python
import numpy as np
from src.models.statistical import PrincipalComponentAnalysis

# 生成数据
X = np.random.randn(100, 5)

# 降维
pca = PrincipalComponentAnalysis(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Original shape: {X.shape}")
print(f"Reduced shape: {X_reduced.shape}")
```
