"""
贪心算法模块

实现各种经典贪心算法问题
"""

from typing import List, Tuple


def activity_selection(start_times: List[int], end_times: List[int]) -> List[int]:
    """
    活动选择问题
    
    Args:
        start_times: 活动开始时间列表
        end_times: 活动结束时间列表
        
    Returns:
        选中的活动索引列表
    """
    activities = list(zip(range(len(start_times)), start_times, end_times))
    activities.sort(key=lambda x: x[2])
    
    selected = [activities[0][0]]
    last_end_time = activities[0][2]
    
    for i, start, end in activities[1:]:
        if start >= last_end_time:
            selected.append(i)
            last_end_time = end
    
    return selected


def fractional_knapsack(weights: List[float], values: List[float], capacity: float) -> float:
    """
    分数背包问题
    
    Args:
        weights: 物品重量列表
        values: 物品价值列表
        capacity: 背包容量
        
    Returns:
        最大价值
    """
    items = [(v / w, w, v) for v, w in zip(values, weights)]
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for ratio, weight, value in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += ratio * remaining_capacity
            break
    
    return total_value


def huffman_encoding(frequencies: List[Tuple[str, int]]) -> dict:
    """
    哈夫曼编码
    
    Args:
        frequencies: 字符及其频率的列表
        
    Returns:
        字符到编码的映射字典
    """
    import heapq
    
    if not frequencies:
        return {}
    
    heap = [[freq, [char, ""]] for char, freq in frequencies]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return {char: code for char, code in heap[0][1:]}


__all__ = [
    "activity_selection",
    "fractional_knapsack",
    "huffman_encoding",
]
