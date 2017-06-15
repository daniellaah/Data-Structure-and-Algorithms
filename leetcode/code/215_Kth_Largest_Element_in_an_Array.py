"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

# 解法一: 使用partition
from random import randint

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums:
            pivot_idx = self.partition(nums, randint(0, len(nums)-1))
            if k - 1 < pivot_idx:
                return self.findKthLargest(nums[0: pivot_idx], k)
            elif k - 1 > pivot_idx:
                return self.findKthLargest(nums[pivot_idx+1:], k - (pivot_idx+1))
            else:
                return nums[pivot_idx]

    def partition(self, nums, pivot_idx):
        nums[pivot_idx], nums[0] = nums[0], nums[pivot_idx]
        pivot_idx = 0
        store_idx = pivot_idx + 1
        for i in range(store_idx, len(nums)):
            if nums[i] > nums[pivot_idx]:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
        nums[store_idx-1], nums[pivot_idx] = nums[pivot_idx], nums[store_idx-1]
        return store_idx - 1

# 解法二: 使用最小堆
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.make_min_heap(nums, k)
        for i in range(k, len(nums)):
            if nums[i] > nums[0]:
                nums[i], nums[0] = nums[0], nums[i]
                self.arrangeDown(nums, 0, k)
        return nums[0]

    def make_min_heap(self, nums, k):
        for i in range((k-1) // 2, -1, -1):
            self.arrangeDown(nums, i, k)

    def arrangeDown(self, nums, i, k):
        j = 2 * i + 1
        while j < k:
            if j + 1 < k and nums[j+1] < nums[j]:
                j += 1
            if nums[j] >= nums[i]:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i = j
            j = 2 * i + 1
