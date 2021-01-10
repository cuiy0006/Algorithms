class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        buy = prices[0]
        i = 1
        while i < len(prices):
            if prices[i] > buy:
                profit += prices[i] - buy
            buy = prices[i]
            i += 1
        return profit
