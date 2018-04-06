class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        buy = sys.maxsize
        
        for price in prices:
            buy = min(price, buy)
            maxProfit = max(maxProfit, price - buy)
        return maxProfit
