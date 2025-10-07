class Solution:
    # def getRow(self, rowIndex: int) -> List[int]:
    #     dp = []
    #     for i in range(rowIndex+1):
    #         dp.append([1] * (i+1))
    #         for j in  range (1, i):
    #             dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    #     return dp[rowIndex]

    # def getRow(self, rowIndex: int) -> List[int]:
    #     if rowIndex == 0:
    #         return [1]
    #     curRow = [1]
    #     dp = [1]
    #     for i in range(1, rowIndex+1):
    #         curRow = [1] * (i+1)
    #         for j in  range (1, i):
    #             curRow[j] = dp[j-1] + dp[j]
    #         dp = curRow
    #     return curRow

    # def getRow(self, rowIndex: int) -> List[int]:
    #     dp = [1]
    #     for i in range(rowIndex):
    #         dp.append(1)
    #         for j in range(len(dp)-2, 0, -1):
    #             dp[j] += dp[j-1]
    #     return dp