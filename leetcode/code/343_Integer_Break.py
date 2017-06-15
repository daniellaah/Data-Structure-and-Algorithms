"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58."""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 7:
            return (n//2) * (n-n//2)
        else:
            if (n-5) % 3 == 0:
                return pow(3, (n-5)//3)*6
            if (n-6) % 3 == 0:
                return pow(3, (n-6)//3)*9
            if (n-7) % 3 == 0:
                return pow(3, (n-7)//3)*12
