class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            dp.append([1] * (i + 1))
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp