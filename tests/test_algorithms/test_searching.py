"""
搜索算法测试
"""

import pytest
from src.algorithms.searching import binary_search, linear_search


class TestSearchingAlgorithms:
    
    def test_binary_search_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13]
        assert binary_search(arr, 7) == 3
    
    def test_binary_search_not_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13]
        assert binary_search(arr, 6) == -1
    
    def test_linear_search_found(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        assert linear_search(arr, 22) == 4
    
    def test_linear_search_not_found(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        assert linear_search(arr, 100) == -1
    
    def test_empty_array(self):
        arr = []
        assert binary_search(arr, 5) == -1
        assert linear_search(arr, 5) == -1
