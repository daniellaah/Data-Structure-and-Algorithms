"""53. Maximum Subarray
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
# DP
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        f = nums
        ret = f[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i-1] + nums[i], nums[i])
            ret = max(ret, f[i])
        return ret

# Greedy
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sum = 0
        ans = nums[0]
        for n in nums:
            sum += n
            ans = max(ans, sum)
            sum = max(0, sum)
        return ans
