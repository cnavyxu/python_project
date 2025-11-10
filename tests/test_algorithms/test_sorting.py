"""
排序算法测试
"""

import pytest
from src.algorithms.sorting import quick_sort, merge_sort, bubble_sort


class TestSortingAlgorithms:
    
    def test_quick_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = quick_sort(arr)
        assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_merge_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = merge_sort(arr)
        assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_bubble_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = bubble_sort(arr)
        assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_empty_array(self):
        arr = []
        assert quick_sort(arr) == []
        assert merge_sort(arr) == []
        assert bubble_sort(arr) == []
    
    def test_single_element(self):
        arr = [42]
        assert quick_sort(arr) == [42]
        assert merge_sort(arr) == [42]
        assert bubble_sort(arr) == [42]
    
    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        assert quick_sort(arr) == [1, 2, 3, 4, 5]
        assert merge_sort(arr) == [1, 2, 3, 4, 5]
        assert bubble_sort(arr) == [1, 2, 3, 4, 5]
