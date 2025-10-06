from typing import List


class SolutionBruteForce:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit


class SolutionDivideAndConquer:
    """
    Time Complexity: O(n)
    Space Complexity: O(log n)
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        def helper(i: int, j: int) -> tuple[int, int, int]:
            """
            Returns: (max_profit, min_price, max_price) in the range [i, j]
            """
            if i == j:
                return 0, prices[i], prices[i]

            mid = i + (j - i) // 2
            max_profit_left, min_price_left, max_price_left = helper(i, mid)
            max_profit_right, min_price_right, max_price_right = helper(mid + 1, j)

            max_profit = max(
                max_profit_left,
                max_profit_right,
                max_price_right - min_price_left
            )
            min_price = min(min_price_left, min_price_right)
            max_price = max(max_price_left, max_price_right)

            return max_profit, min_price, max_price

        max_profit, _, _ = helper(0, len(prices) - 1)
        return max_profit


class SolutionOnePass:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit