'''Closest Number in Sorted Array
Given a target number and an integer array A sorted in ascending order,
find the index i in A such that A[i] is closest to the given target.
Return -1 if there is no element in the array.
Example
Given [1, 2, 3] and target = 2, return 1.
Given [1, 4, 6] and target = 3, return 1.
Given [1, 4, 6] and target = 5, return 1 or 2.
Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.
'''
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        # Write your code here
        if not A or not target:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            middle = start + (end - start) // 2
            if A[middle] == target:
                return middle
            elif A[middle] < target:
                start = middle
            else:
                end = middle
        return end if abs(A[start] - target) > abs(A[end] - target) else start
