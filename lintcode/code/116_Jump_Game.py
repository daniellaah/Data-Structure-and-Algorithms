'''Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
# 解法一: DP
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        dp = [False for i in range(len(A))]
        dp[0] = True
        for i in range(1, len(A)):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
        return dp[-1]

# 解法二: Greedy
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        i, rightMost = 0, 0
        for s in A[:-1]:
            rightMost = max(rightMost, i + s)
            if rightMost <= i:
                return False
            i += 1
        return True
