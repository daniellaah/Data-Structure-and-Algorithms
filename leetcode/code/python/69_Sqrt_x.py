"""69. Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = x
        while ans * ans > x:
            ans = (ans + x/ans) / 2
        return ans
