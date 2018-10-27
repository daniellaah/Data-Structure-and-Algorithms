"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.make_max_heap(nums)
        maximun = nums[0]
        tmp = nums[0]
        count = 1
        for i in range(0, len(nums)):
            if tmp != nums[0]:
                count += 1
                if count == 3:
                    return nums[0]
                tmp = nums[0]
            nums[0], nums[-(i+1)] = nums[-(i+1)], nums[0]
            self.arrangeDown(nums, 0, len(nums)-(i+1))
        return maximun

    def make_max_heap(self, nums):
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.arrangeDown(nums, i, len(nums))

    def arrangeDown(self, nums, i, k):
        j = 2 * i + 1
        while j < k:
            if j + 1 < k and nums[j+1] > nums[j]:
                j += 1
            if nums[i] > nums[j]:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i = j
            j = 2 * i + 1
