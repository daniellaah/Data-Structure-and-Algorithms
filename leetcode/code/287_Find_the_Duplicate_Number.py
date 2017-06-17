'''Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''
class Solution(object):
    def countRange(self, start, end):
        count = 0
        for num in self.nums:
            if start <= num <= end:
                count += 1
        return count

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        self.nums = nums
        start, end = 1, len(nums)-1
        middle = (start + end) //2
        while start < end:
            if self.countRange(start, middle) > (middle - start + 1):
                end = middle
            else:
                start = middle + 1
            middle = (start + end) // 2
        return start
