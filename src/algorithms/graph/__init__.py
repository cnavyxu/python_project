"""
图算法模块

实现各种经典图算法
"""

from typing import Dict, List, Set, Tuple, Optional
from collections import deque, defaultdict
import heapq


class Graph:
    """图的基本表示"""
    
    def __init__(self, directed: bool = False):
        self.graph: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u: int, v: int, weight: float = 1.0):
        """添加边"""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def bfs(self, start: int) -> List[int]:
        """
        广度优先搜索
        
        Args:
            start: 起始节点
            
        Returns:
            遍历顺序
        """
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs(self, start: int) -> List[int]:
        """
        深度优先搜索
        
        Args:
            start: 起始节点
            
        Returns:
            遍历顺序
        """
        visited = set()
        result = []
        
        def _dfs(node: int):
            visited.add(node)
            result.append(node)
            for neighbor, _ in self.graph[node]:
                if neighbor not in visited:
                    _dfs(neighbor)
        
        _dfs(start)
        return result
    
    def dijkstra(self, start: int) -> Dict[int, float]:
        """
        Dijkstra最短路径算法
        
        Args:
            start: 起始节点
            
        Returns:
            从起始节点到各节点的最短距离
        """
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            for neighbor, weight in self.graph[current]:
                distance = current_dist + weight
                
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances


__all__ = [
    "Graph",
]
