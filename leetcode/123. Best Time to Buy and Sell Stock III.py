class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [-prices[0], 0, -prices[0], 0]
        dp2 = [0, 0, 0, 0]

        for i in range(1, len(prices)):
            price = prices[i]
            dp2[0] = max(dp1[0], -price)
            dp2[1] = max(dp1[1], dp1[0] + price)
            dp2[2] = max(dp1[2], dp1[1] - price)
            dp2[3] = max(dp1[3], dp1[2] + price)
            dp1, dp2 = dp2, [0, 0, 0, 0]
        
        return max(dp1)
