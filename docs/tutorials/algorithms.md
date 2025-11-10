# 算法教程

本教程介绍如何使用项目中实现的各种算法。

## 排序算法

### 快速排序

```python
from src.algorithms.sorting import quick_sort

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### 归并排序

```python
from src.algorithms.sorting import merge_sort

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
```

## 搜索算法

### 二分搜索

```python
from src.algorithms.searching import binary_search

arr = [1, 3, 5, 7, 9, 11, 13]
index = binary_search(arr, 7)
print(index)  # 3
```

## 图算法

### 广度优先搜索 (BFS)

```python
from src.algorithms.graph import Graph

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

traversal = g.bfs(0)
print(traversal)  # [0, 1, 2, 3]
```

### Dijkstra最短路径

```python
from src.algorithms.graph import Graph

g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)

distances = g.dijkstra(0)
print(distances)  # {0: 0, 2: 1, 1: 3, 3: 4}
```

## 动态规划

### 斐波那契数列

```python
from src.algorithms.dynamic_programming import fibonacci

result = fibonacci(10)
print(result)  # 55
```

### 0-1背包问题

```python
from src.algorithms.dynamic_programming import knapsack_01

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

max_value = knapsack_01(weights, values, capacity)
print(max_value)  # 10
```

## 贪心算法

### 活动选择问题

```python
from src.algorithms.greedy import activity_selection

start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

selected = activity_selection(start_times, end_times)
print(selected)  # [0, 1, 3, 4]
```

## 回溯算法

### N皇后问题

```python
from src.algorithms.backtracking import n_queens

solutions = n_queens(4)
for solution in solutions:
    for row in solution:
        print(row)
    print()
```

### 全排列

```python
from src.algorithms.backtracking import permutations

nums = [1, 2, 3]
result = permutations(nums)
print(result)  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], ...]
```
