'''Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

 Notice

All costs are positive integers.
Example
Given costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

house 0 is blue, house 1 is green, house 2 is blue, 2 + 5 + 3 = 10
'''


import sys
MAX_VALUE = sys.maxsize
class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        if not costs or not costs[0]:
            return 0
        m, k = len(costs) + 1, len(costs[0])
        dp = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(k):
            dp[0][i] = 0
        for i in range(1, m):
            for j in range(k):
                dp[i][j] = MAX_VALUE
                for c in range(k):
                    if j != c:
                        dp[i][j] = min(dp[i][j], dp[i-1][c])
                dp[i][j] += costs[i-1][j]
        return min(dp[m-1])
