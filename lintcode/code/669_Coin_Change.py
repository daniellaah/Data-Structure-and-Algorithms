'''Coin Change
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
Example
Given coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Given coins = [2], amount = 3
return -1.
'''
import sys
MAX_VALUE = sys.maxsize
class Solution:
    # @param {int[]} coins  a list of integer
    # @param {int} amount a total amount of money amount
    # @return {int} the fewest number of coins that you need to make up
    def coinChange(self, coins , amount):
        # Write your code here
        if not coins or amount is None:
            return -1
        dp = [0 for _ in range(amount+1)]
        for i in range(1, amount+1):
            dp[i] = MAX_VALUE
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != MAX_VALUE else -1
