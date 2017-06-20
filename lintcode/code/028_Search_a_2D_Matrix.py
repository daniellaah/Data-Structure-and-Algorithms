'''Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
'''
# 方法一, 两次二分搜索
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0] or not target:
            return False
        row_start, row_end = 0, len(matrix) - 1
        while row_start + 1 < row_end:
            middle = row_start + (row_end - row_start) // 2
            if matrix[middle][-1] == target:
                return True
            elif matrix[middle][-1] > target:
                row_end = middle
            else:
                row_start = middle
        if matrix[row_start][-1] == target or matrix[row_end][-1] == target:
            return True
        if matrix[row_start][-1] > target:
            row = row_start
        else:
            row = row_end

        start, end = 0, len(matrix[row]) - 1
        while start + 1 < end:
            middle = start + (end - start) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                end = middle
            else:
                start = middle
        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        return False

# 方法二, 一次二分
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0] or not target:
            return False
        row_num, col_num = len(matrix), len(matrix[0])
        start, end = 0, row_num * col_num - 1
        while start + 1 < end:
            middle = start + (end - start) // 2
            if matrix[middle // col_num][middle % col_num] == target:
                return True
            elif matrix[middle // col_num][middle % col_num] > target:
                end = middle
            else:
                start = middle
        if matrix[start // col_num][start % col_num] == target:
            return True
        if matrix[end // col_num][end % col_num] == target:
            return True
        return False
