"""
回溯算法模块

实现各种经典回溯算法问题
"""

from typing import List


def n_queens(n: int) -> List[List[str]]:
    """
    N皇后问题
    
    Args:
        n: 棋盘大小
        
    Returns:
        所有可能的解决方案
    """
    def is_safe(board: List[int], row: int, col: int) -> bool:
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def solve(board: List[int], row: int):
        if row == n:
            result.append(['.' * col + 'Q' + '.' * (n - col - 1) for col in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
    
    result = []
    solve([-1] * n, 0)
    return result


def sudoku_solver(board: List[List[str]]) -> bool:
    """
    数独求解器
    
    Args:
        board: 9x9的数独棋盘
        
    Returns:
        是否成功求解
    """
    def is_valid(row: int, col: int, num: str) -> bool:
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    def solve() -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    return solve()


def permutations(nums: List[int]) -> List[List[int]]:
    """
    全排列
    
    Args:
        nums: 数字列表
        
    Returns:
        所有可能的排列
    """
    def backtrack(path: List[int]):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()
    
    result = []
    backtrack([])
    return result


def combinations(n: int, k: int) -> List[List[int]]:
    """
    组合
    
    Args:
        n: 范围1到n
        k: 选择k个数字
        
    Returns:
        所有可能的组合
    """
    def backtrack(start: int, path: List[int]):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    result = []
    backtrack(1, [])
    return result


__all__ = [
    "n_queens",
    "sudoku_solver",
    "permutations",
    "combinations",
]
