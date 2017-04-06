"""204. Count Primes
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [1 for i in range(n)]
        i = 2
        while i * i < n:
            if not isPrime[i]:
                continue
            for j in range(i * i, n, i):
                if j % i == 0:
                    isPrime[j] = False
            i += 1
        return sum(isPrime[2:])
