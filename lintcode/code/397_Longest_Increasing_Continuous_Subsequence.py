'''397_Longest_Increasing_Continuous_Subsequence
Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.
Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
'''

class Solution:
    # @param {int[]} nums an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, nums):
        # Write your code here
        if not nums:
            return 0
        length = len(nums)
        dpIncreasing = [1 for i in range(length)]
        dpDecreasing = [1 for i in range(length)]
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                dpIncreasing[i] = dpIncreasing[i-1] + 1
            if nums[i] < nums[i-1]:
                dpDecreasing[i] = dpDecreasing[i-1] + 1
        return max(dpIncreasing+dpDecreasing)
