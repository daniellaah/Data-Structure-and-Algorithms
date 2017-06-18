"""Longest Common Substring
Given two strings, find the longest common substring.

Return the length of it.

 Notice

The characters in substring should occur continuously in original string. This is different with subsequence.
Example
Given A = "ABCD", B = "CBCE", return 2.
"""
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        m, n = len(A), len(B)
        f = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(0, m):
            for j in range(0, n):
                if A[i] == B[j]:
                    f[i+1][j+1] = f[i][j] + 1
        return max(map(max, f))
