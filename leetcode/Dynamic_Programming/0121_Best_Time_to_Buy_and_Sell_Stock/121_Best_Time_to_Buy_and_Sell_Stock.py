class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     max_profit, min_price = 0, float("inf")
    #     for price in prices:
    #         min_price = min(min_price, price)
    #         max_profit = max(max_profit, price - min_price)
    #     return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")
        for price in prices:
                min_price = price if min_price > price else min_price
                max_profit = price - min_price if max_profit < price - min_price else max_profit
        return max_profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     dp = [0] * len(prices)
    #     min_price = prices[0]
    #     for i in range(1, len(prices)):
    #         min_price = min(min_price, prices[i])
    #         dp[i] = max(dp[i-1], prices[i] - min_price)
    #     return dp[-1]
