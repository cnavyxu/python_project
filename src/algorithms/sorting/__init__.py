"""
排序算法模块

实现各种经典排序算法
"""

from typing import List, TypeVar, Callable, Optional

T = TypeVar('T')


def quick_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    快速排序
    
    Args:
        arr: 待排序数组
        key: 排序关键字函数
        
    Returns:
        排序后的数组
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    pivot_key = key(pivot) if key else pivot
    
    left = [x for x in arr if (key(x) if key else x) < pivot_key]
    middle = [x for x in arr if (key(x) if key else x) == pivot_key]
    right = [x for x in arr if (key(x) if key else x) > pivot_key]
    
    return quick_sort(left, key) + middle + quick_sort(right, key)


def merge_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    归并排序
    
    Args:
        arr: 待排序数组
        key: 排序关键字函数
        
    Returns:
        排序后的数组
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    
    return _merge(left, right, key)


def _merge(left: List[T], right: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """合并两个有序数组"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_key = key(left[i]) if key else left[i]
        right_key = key(right[j]) if key else right[j]
        
        if left_key <= right_key:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def bubble_sort(arr: List[T], key: Optional[Callable[[T], any]] = None) -> List[T]:
    """
    冒泡排序
    
    Args:
        arr: 待排序数组
        key: 排序关键字函数
        
    Returns:
        排序后的数组
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            val_j = key(arr[j]) if key else arr[j]
            val_j1 = key(arr[j + 1]) if key else arr[j + 1]
            
            if val_j > val_j1:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


__all__ = [
    "quick_sort",
    "merge_sort",
    "bubble_sort",
]
