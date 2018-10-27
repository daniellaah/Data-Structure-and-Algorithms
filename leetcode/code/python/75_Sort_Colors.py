"""75. Sort Colors
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
# 解法一
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        head, tail, i = 0, len(nums) - 1, 0
        while i <= tail:
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                if i == head:
                    i += 1
                head += 1
            elif nums[i] == 2:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1
            else:
                i += 1
# 解法二, hash, count
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        hash = [0] * 3
        for num in nums:
            hash[num] += 1
        index = 0
        for i in range(len(hash)):
            for j in range(hash[i]):
                nums[index] = i
                index += 1
