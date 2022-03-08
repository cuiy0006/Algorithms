class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0. not hold do nothing
        # 1. not hold buy
        # 2. hold do nothing
        # 3. hold sell
        dp1 = [0, -prices[0], -prices[0], 0]
        dp2 = [0, 0, 0, 0]
        
        for i in range(1, len(prices)):
            price = prices[i]
            dp2[0] = max(dp1[0], dp1[3])
            dp2[1] = dp1[0] - price
            dp2[2] = max(dp1[1], dp1[2])
            dp2[3] = max(dp1[1] + price, dp1[2] + price)
            
            dp1, dp2 = dp2, [0, 0, 0, 0]

        return max(dp1)
        
