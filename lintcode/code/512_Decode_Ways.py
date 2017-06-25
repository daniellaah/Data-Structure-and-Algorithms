'''Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
Example
Given encoded message 12, it could be decoded as AB (1 2) or L (12).
The number of ways decoding 12 is 2.
'''
class Solution:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        # Write your code here
        if not s:
            return 0
        length = len(s) + 1
        dp = [0 for _ in range(length)]
        dp[0] = 1
        for i in range(1, length):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and ((s[i-2] == '1') or (s[i-2] == '2' and '0' <= s[i-1] <= '6')):
                dp[i] += dp[i-2]
        return dp[length-1]
