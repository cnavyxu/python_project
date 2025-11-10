"""
API 数据模型（Pydantic Schemas）
"""

from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """健康检查响应"""

    status: str = Field(..., description="服务状态")
    version: str = Field(..., description="版本号")


class SortRequest(BaseModel):
    """排序请求"""

    data: List[float] = Field(..., description="待排序数组")
    algorithm: str = Field("quick_sort", description="排序算法名称")
    reverse: bool = Field(False, description="是否降序")


class SortResponse(BaseModel):
    """排序响应"""

    sorted_data: List[float] = Field(..., description="排序后的数组")
    algorithm: str = Field(..., description="使用的算法")
    execution_time: float = Field(..., description="执行时间（秒）")


class SearchRequest(BaseModel):
    """搜索请求"""

    data: List[float] = Field(..., description="搜索数组")
    target: float = Field(..., description="目标值")
    algorithm: str = Field("binary_search", description="搜索算法名称")


class SearchResponse(BaseModel):
    """搜索响应"""

    index: int = Field(..., description="目标索引，-1 表示未找到")
    algorithm: str = Field(..., description="使用的算法")
    execution_time: float = Field(..., description="执行时间（秒）")


class PredictRequest(BaseModel):
    """预测请求"""

    model_type: str = Field(..., description="模型类型")
    features: List[List[float]] = Field(..., description="特征数据")
    model_params: Optional[Dict[str, Any]] = Field(None, description="模型参数")


class PredictResponse(BaseModel):
    """预测响应"""

    predictions: List[float] = Field(..., description="预测结果")
    model_type: str = Field(..., description="模型类型")
    execution_time: float = Field(..., description="执行时间（秒）")


class TrainRequest(BaseModel):
    """训练请求"""

    model_type: str = Field(..., description="模型类型")
    X_train: List[List[float]] = Field(..., description="训练特征")
    y_train: List[float] = Field(..., description="训练标签")
    model_params: Optional[Dict[str, Any]] = Field(None, description="模型参数")


class TrainResponse(BaseModel):
    """训练响应"""

    message: str = Field(..., description="训练结果消息")
    model_type: str = Field(..., description="模型类型")
    execution_time: float = Field(..., description="执行时间（秒）")
    metrics: Optional[Dict[str, float]] = Field(None, description="训练指标")


class ErrorResponse(BaseModel):
    """错误响应"""

    detail: str = Field(..., description="错误详情")
    error: Optional[str] = Field(None, description="错误信息")
