"""
排序算法示例

演示如何使用各种排序算法
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.algorithms.sorting import quick_sort, merge_sort, bubble_sort
from src.utils import timer


@timer
def demo_quick_sort():
    """快速排序演示"""
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    print(f"原始数组: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"快速排序结果: {sorted_arr}")
    return sorted_arr


@timer
def demo_merge_sort():
    """归并排序演示"""
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    print(f"原始数组: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"归并排序结果: {sorted_arr}")
    return sorted_arr


@timer
def demo_bubble_sort():
    """冒泡排序演示"""
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    print(f"原始数组: {arr}")
    sorted_arr = bubble_sort(arr)
    print(f"冒泡排序结果: {sorted_arr}")
    return sorted_arr


if __name__ == "__main__":
    print("=" * 50)
    print("排序算法演示")
    print("=" * 50)
    
    print("\n1. 快速排序:")
    demo_quick_sort()
    
    print("\n2. 归并排序:")
    demo_merge_sort()
    
    print("\n3. 冒泡排序:")
    demo_bubble_sort()
