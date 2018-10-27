"""50. Pow(x, n)
Implement pow(x, n)."""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x

        # if -0.0000001 < x - 0.0 < 0.0000001 and n < 0:
        #     return 0.0

        if n < 0:
            n = -n
            x = 1/x
        ret = 1.0
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x, (n-1)/2)
