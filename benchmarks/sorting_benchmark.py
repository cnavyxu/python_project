"""
排序算法性能基准测试

比较不同排序算法的性能
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import time
import numpy as np
from src.algorithms.sorting import quick_sort, merge_sort, bubble_sort


def benchmark_sorting_algorithm(sort_func, arr, name):
    """基准测试单个排序算法"""
    arr_copy = arr.copy()
    start_time = time.time()
    sorted_arr = sort_func(arr_copy.tolist())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{name:15} - 耗时: {elapsed_time:.6f} 秒")
    return elapsed_time


def run_benchmark(size=1000):
    """运行排序算法基准测试"""
    print(f"\n{'='*50}")
    print(f"排序算法性能基准测试 (数组大小: {size})")
    print(f"{'='*50}\n")
    
    np.random.seed(42)
    arr = np.random.randint(0, 10000, size=size)
    
    results = {}
    
    print("随机数组测试:")
    print("-" * 50)
    results['quick_sort'] = benchmark_sorting_algorithm(quick_sort, arr, "快速排序")
    results['merge_sort'] = benchmark_sorting_algorithm(merge_sort, arr, "归并排序")
    
    if size <= 1000:
        results['bubble_sort'] = benchmark_sorting_algorithm(bubble_sort, arr, "冒泡排序")
    else:
        print(f"{'冒泡排序':15} - 跳过（数组过大）")
    
    arr_sorted = np.sort(arr)
    print(f"\n已排序数组测试:")
    print("-" * 50)
    benchmark_sorting_algorithm(quick_sort, arr_sorted, "快速排序")
    benchmark_sorting_algorithm(merge_sort, arr_sorted, "归并排序")
    
    arr_reversed = arr_sorted[::-1]
    print(f"\n逆序数组测试:")
    print("-" * 50)
    benchmark_sorting_algorithm(quick_sort, arr_reversed, "快速排序")
    benchmark_sorting_algorithm(merge_sort, arr_reversed, "归并排序")
    
    print(f"\n{'='*50}")
    print("基准测试完成")
    print(f"{'='*50}\n")
    
    return results


if __name__ == "__main__":
    print("开始性能基准测试...")
    
    run_benchmark(size=100)
    run_benchmark(size=1000)
    run_benchmark(size=5000)
