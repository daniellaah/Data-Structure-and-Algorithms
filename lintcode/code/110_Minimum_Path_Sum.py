'''Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

 Notice

You can only move either down or right at any point in time.
'''
import sys
MAX_VALUE = sys.maxsize
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = MAX_VALUE
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                dp[i][j] += grid[i][j]
        return dp[m-1][n-1]
