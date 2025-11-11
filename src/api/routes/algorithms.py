"""
算法相关路由
"""

import time
from typing import List
from fastapi import APIRouter, HTTPException

from ...logging import get_logger
from ..schemas import SortRequest, SortResponse, SearchRequest, SearchResponse

logger = get_logger("api.algorithms")

router = APIRouter()


def quick_sort(arr: List[float], reverse: bool = False) -> List[float]:
    """快速排序实现"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    if not reverse:
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
    else:
        left = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
    return quick_sort(left, reverse) + middle + quick_sort(right, reverse)


def bubble_sort(arr: List[float], reverse: bool = False) -> List[float]:
    """冒泡排序实现"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1] and not reverse) or (
                arr[j] < arr[j + 1] and reverse
            ):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr: List[float], target: float) -> int:
    """二分搜索实现（假设数组已排序）"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linear_search(arr: List[float], target: float) -> int:
    """线性搜索实现"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


SORT_ALGORITHMS = {
    "quick_sort": quick_sort,
    "bubble_sort": bubble_sort,
}

SEARCH_ALGORITHMS = {
    "binary_search": binary_search,
    "linear_search": linear_search,
}


@router.post("/sort", response_model=SortResponse)
async def sort_array(request: SortRequest):
    """
    数组排序端点

    支持多种排序算法
    """
    logger.info(f"排序请求: 算法={request.algorithm}, 数据长度={len(request.data)}")

    if request.algorithm not in SORT_ALGORITHMS:
        logger.error(f"不支持的排序算法: {request.algorithm}")
        raise HTTPException(status_code=400, detail=f"不支持的排序算法: {request.algorithm}")

    try:
        start_time = time.time()
        sorted_data = SORT_ALGORITHMS[request.algorithm](request.data, request.reverse)
        execution_time = time.time() - start_time

        logger.info(f"排序完成: 耗时={execution_time:.4f}秒")

        return SortResponse(
            sorted_data=sorted_data,
            algorithm=request.algorithm,
            execution_time=execution_time,
        )
    except Exception as e:
        logger.error(f"排序失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"排序失败: {str(e)}")


@router.post("/search", response_model=SearchResponse)
async def search_array(request: SearchRequest):
    """
    数组搜索端点

    支持多种搜索算法
    """
    logger.info(f"搜索请求: 算法={request.algorithm}, 目标={request.target}")

    if request.algorithm not in SEARCH_ALGORITHMS:
        logger.error(f"不支持的搜索算法: {request.algorithm}")
        raise HTTPException(status_code=400, detail=f"不支持的搜索算法: {request.algorithm}")

    try:
        start_time = time.time()
        index = SEARCH_ALGORITHMS[request.algorithm](request.data, request.target)
        execution_time = time.time() - start_time

        logger.info(f"搜索完成: 结果索引={index}, 耗时={execution_time:.4f}秒")

        return SearchResponse(
            index=index, algorithm=request.algorithm, execution_time=execution_time
        )
    except Exception as e:
        logger.error(f"搜索失败: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"搜索失败: {str(e)}")


@router.get("/algorithms/sort")
async def list_sort_algorithms():
    """
    列出可用的排序算法
    """
    return {"algorithms": list(SORT_ALGORITHMS.keys())}


@router.get("/algorithms/search")
async def list_search_algorithms():
    """
    列出可用的搜索算法
    """
    return {"algorithms": list(SEARCH_ALGORITHMS.keys())}
