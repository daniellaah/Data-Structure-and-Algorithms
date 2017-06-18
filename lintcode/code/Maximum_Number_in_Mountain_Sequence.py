'''Maximum Number in Mountain Sequence
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.
Example
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10
'''
class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = start + (end - start) // 2
            if nums[middle-1] < nums[middle] > nums[middle+1]:
                return nums[middle]
            elif nums[middle] < nums[middle+1]:
                start = middle
            else:
                end = middle
        return max(nums[start], nums[end])
