"""34. Search for a Range
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.getFirst(nums, target), self.getLast(nums, target)

    def getFirst(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = end + start // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] == target:
                if (mid > 0 and nums[mid-1] != target) or mid == 0:
                    return mid
                else:
                    end = mid -1
            else:
                start = mid + 1
        return -1

    def getLast(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        mid = end + start // 2
        while start <= end:
            mid = end - start // 2 + start
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] == target:
                if  (mid < len(nums)-1 and nums[mid+1] != target) or mid == len(nums)-1:
                    return mid
                else:
                    start = mid + 1
            else:
                start = mid + 1
        return -1
