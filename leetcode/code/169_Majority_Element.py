"""Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array."""

# 解法一: hash
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            return nums[0]
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
                if dic[num] > size // 2:
                    return num
            else:
                dic[num] = 1

# 解法二: Boyer-Moore Majority Vote Algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                count += 1
                major = num
            else:
                if major == num:
                    count += 1
                else:
                    count -= 1
        return major
