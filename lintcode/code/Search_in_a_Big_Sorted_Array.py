'''Search in a Big Sorted Array
Given a big sorted array with positive integers sorted by ascending order.
The array is so big so that you can not get the length of the whole array directly,
and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
Find the first index of a target number. Your algorithm should be in O(log k),
where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.

Example
Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.
'''
"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if not reader or not target:
            return -1
        k = 1
        while reader.get(k-1) < target:
            k = k * 2
        start, end = k // 2 - 1, k - 1
        while start + 1 < end:
            middle = start + (end - start) // 2
            if reader.get(middle) >= target:
                end = middle
            else:
                start = middle
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
