class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        buy = sys.maxsize
        for i, price in enumerate(prices):
            buy = min(buy, price)
            if i == len(prices) - 1 or price > prices[i+1]:
                total += price - buy
                buy = price
        return total
