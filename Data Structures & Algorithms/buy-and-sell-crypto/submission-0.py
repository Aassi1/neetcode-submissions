class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, maximum = prices[0], 0

        for num in prices:
            profit_today = num - minimum
            maximum = max(maximum, profit_today)
            minimum = min(num, minimum)

        return maximum

        