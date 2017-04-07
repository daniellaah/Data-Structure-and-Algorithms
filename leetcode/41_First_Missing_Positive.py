"""41. First Missing Positive
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        size = len(nums)
        for i in range(size):
            while nums[i] > 0 and nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i] X
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1
