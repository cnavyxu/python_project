"""
模型相关路由
"""

import time
import numpy as np
from typing import Dict, Any
from fastapi import APIRouter, HTTPException

from ...logging import get_logger
from ..schemas import PredictRequest, PredictResponse, TrainRequest, TrainResponse

logger = get_logger("api.models")

router = APIRouter()


class SimpleLinearRegression:
    """简单线性回归模型"""

    def __init__(self):
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """训练模型"""
        X = np.array(X)
        y = np.array(y)
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)

        X_mean = np.mean(X, axis=0)
        y_mean = np.mean(y)

        numerator = np.sum((X - X_mean) * (y - y_mean).reshape(-1, 1), axis=0)
        denominator = np.sum((X - X_mean) ** 2, axis=0)

        self.weights = numerator / (denominator + 1e-8)
        self.bias = y_mean - np.dot(X_mean, self.weights)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """预测"""
        X = np.array(X)
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)
        return np.dot(X, self.weights) + self.bias


class SimpleKNN:
    """简单 K 近邻分类器"""

    def __init__(self, k: int = 3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """训练模型"""
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """预测"""
        X = np.array(X)
        predictions = []

        for x in X:
            distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
            k_indices = np.argsort(distances)[: self.k]
            k_nearest_labels = self.y_train[k_indices]
            most_common = np.bincount(k_nearest_labels.astype(int)).argmax()
            predictions.append(most_common)

        return np.array(predictions)


_models: Dict[str, Any] = {}


@router.post("/train", response_model=TrainResponse)
async def train_model(request: TrainRequest):
    """
    模型训练端点

    训练指定类型的模型
    """
    logger.info(f"训练请求: 模型类型={request.model_type}")

    try:
        start_time = time.time()

        X_train = np.array(request.X_train)
        y_train = np.array(request.y_train)

        if request.model_type == "linear_regression":
            model = SimpleLinearRegression()
            model.fit(X_train, y_train)
            _models[request.model_type] = model

            y_pred = model.predict(X_train)
            mse = np.mean((y_train - y_pred) ** 2)
            metrics = {"mse": float(mse)}

        elif request.model_type == "knn":
            k = request.model_params.get("k", 3) if request.model_params else 3
            model = SimpleKNN(k=k)
            model.fit(X_train, y_train)
            _models[request.model_type] = model

            y_pred = model.predict(X_train)
            accuracy = np.mean(y_train == y_pred)
            metrics = {"accuracy": float(accuracy)}

        else:
            logger.error(f"不支持的模型类型: {request.model_type}")
            raise HTTPException(
                status_code=400, detail=f"不支持的模型类型: {request.model_type}"
            )

        execution_time = time.time() - start_time
        logger.info(f"训练完成: 耗时={execution_time:.4f}秒, 指标={metrics}")

        return TrainResponse(
            message="模型训练成功",
            model_type=request.model_type,
            execution_time=execution_time,
            metrics=metrics,
        )

    except Exception as e:
        logger.error(f"训练失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"训练失败: {str(e)}")


@router.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    """
    模型预测端点

    使用已训练的模型进行预测
    """
    logger.info(f"预测请求: 模型类型={request.model_type}")

    if request.model_type not in _models:
        logger.error(f"模型未训练: {request.model_type}")
        raise HTTPException(status_code=400, detail=f"模型未训练: {request.model_type}")

    try:
        start_time = time.time()

        model = _models[request.model_type]
        X = np.array(request.features)
        predictions = model.predict(X)

        execution_time = time.time() - start_time
        logger.info(f"预测完成: 耗时={execution_time:.4f}秒")

        return PredictResponse(
            predictions=predictions.tolist(),
            model_type=request.model_type,
            execution_time=execution_time,
        )

    except Exception as e:
        logger.error(f"预测失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"预测失败: {str(e)}")


@router.get("/models")
async def list_models():
    """
    列出可用的模型类型
    """
    return {
        "available_models": ["linear_regression", "knn"],
        "trained_models": list(_models.keys()),
    }


@router.delete("/models/{model_type}")
async def delete_model(model_type: str):
    """
    删除已训练的模型
    """
    if model_type in _models:
        del _models[model_type]
        logger.info(f"模型已删除: {model_type}")
        return {"message": f"模型 {model_type} 已删除"}
    else:
        raise HTTPException(status_code=404, detail=f"模型不存在: {model_type}")
