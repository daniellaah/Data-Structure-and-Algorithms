"""Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space."""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        major1, major2 = 0, 1
        count1, count2 = 0, 0
        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
            elif count1 == 0:
                major1, count1 = num, 1
            elif count2 == 0:
                major2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        return [num for num in (major1, major2) if nums.count(num) > len(nums) // 3]
