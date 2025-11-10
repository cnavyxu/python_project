"""
动态规划算法模块

实现各种经典动态规划问题
"""

from typing import List


def fibonacci(n: int) -> int:
    """
    斐波那契数列（动态规划）
    
    Args:
        n: 第n项
        
    Returns:
        斐波那契数列第n项的值
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0-1背包问题
    
    Args:
        weights: 物品重量列表
        values: 物品价值列表
        capacity: 背包容量
        
    Returns:
        最大价值
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    最长公共子序列
    
    Args:
        text1: 字符串1
        text2: 字符串2
        
    Returns:
        最长公共子序列的长度
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def coin_change(coins: List[int], amount: int) -> int:
    """
    零钱兑换
    
    Args:
        coins: 硬币面额列表
        amount: 目标金额
        
    Returns:
        凑成目标金额所需的最少硬币数量，如果无法凑成则返回-1
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


__all__ = [
    "fibonacci",
    "knapsack_01",
    "longest_common_subsequence",
    "coin_change",
]
