"""
健康检查路由
"""

from fastapi import APIRouter
from ...logging import get_logger
from ..schemas import HealthResponse

logger = get_logger("api.health")

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    健康检查端点

    检查服务是否正常运行
    """
    logger.debug("健康检查请求")
    return HealthResponse(status="healthy", version="0.1.0")


@router.get("/", response_model=HealthResponse)
async def root():
    """
    根路径端点

    返回服务基本信息
    """
    logger.debug("根路径访问")
    return HealthResponse(status="running", version="0.1.0")
