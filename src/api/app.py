"""
FastAPI 应用主入口
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from ..logging import get_logger
from .routes import health, algorithms, models

logger = get_logger("api")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("API 服务启动中...")
    yield
    logger.info("API 服务关闭中...")


app = FastAPI(
    title="算法与模型 API 服务",
    description="提供算法和机器学习模型的 REST API 接口",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"全局异常: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500, content={"detail": "内部服务器错误", "error": str(exc)}
    )


app.include_router(health.router, tags=["健康检查"])
app.include_router(algorithms.router, prefix="/api/v1/algorithms", tags=["算法"])
app.include_router(models.router, prefix="/api/v1/models", tags=["模型"])


if __name__ == "__main__":
    import uvicorn

    logger.info("启动 API 服务...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
