"""152. Maximum Product Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
# 版本1
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][0] = dp[0][1] = res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp[i][0] = max(dp[i-1][0] * nums[i], nums[i])
                dp[i][1] = min(dp[i-1][1] * nums[i], nums[i])
            else:
                dp[i][0] = max(dp[i-1][1] * nums[i], nums[i])
                dp[i][1] = min(dp[i-1][0] * nums[i], nums[i])
            res = max(res, dp[i][0])
        return res

# 版本2
class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][0] = dp[0][1] = res = nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            if nums[i] >= 0:
                dp[x][0] = max(dp[y][0] * nums[i], nums[i])
                dp[x][1] = min(dp[y][1] * nums[i], nums[i])
            else:
                dp[x][0] = max(dp[y][1] * nums[i], nums[i])
                dp[x][1] = min(dp[y][0] * nums[i], nums[i])
            res = max(res, dp[i%2][0])
        return res

# 版本3
class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][0] = dp[0][1] = res = nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][1] * nums[i], dp[y][0] * nums[i], nums[i])
            res = max(res, dp[i%2][0])
        return res
