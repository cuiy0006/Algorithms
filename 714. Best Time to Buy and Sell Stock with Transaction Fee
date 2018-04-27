class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        
        days = len(prices)
        buy = [0] * days
        sell = [0] * days
        
        buy[0] = -prices[0]-fee
        sell[0] = 0
        
        for i in range(1, days):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i] - fee)
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        
        return sell[-1]
