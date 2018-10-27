"""179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        compare = lambda x,y: 1 if x + y < y + x else -1 if x + y > y + x else 0
        str_nums = map(str, nums)
        str_nums.sort(cmp=compare)
        return ''.join(str_nums).lstrip('0') or '0'
