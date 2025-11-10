"""
搜索算法模块

实现各种经典搜索算法
"""

from typing import List, TypeVar, Optional, Callable

T = TypeVar('T')


def binary_search(arr: List[T], target: T, key: Optional[Callable[[T], any]] = None) -> int:
    """
    二分搜索
    
    Args:
        arr: 有序数组
        target: 目标值
        key: 比较关键字函数
        
    Returns:
        目标值的索引，如果不存在则返回-1
    """
    left, right = 0, len(arr) - 1
    target_key = key(target) if key else target
    
    while left <= right:
        mid = (left + right) // 2
        mid_key = key(arr[mid]) if key else arr[mid]
        
        if mid_key == target_key:
            return mid
        elif mid_key < target_key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def linear_search(arr: List[T], target: T) -> int:
    """
    线性搜索
    
    Args:
        arr: 数组
        target: 目标值
        
    Returns:
        目标值的索引，如果不存在则返回-1
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def jump_search(arr: List[T], target: T) -> int:
    """
    跳跃搜索
    
    Args:
        arr: 有序数组
        target: 目标值
        
    Returns:
        目标值的索引，如果不存在则返回-1
    """
    import math
    
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1


__all__ = [
    "binary_search",
    "linear_search",
    "jump_search",
]
