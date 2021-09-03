class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        dp = [[0, 0, 0] for cost in costs]
        dp[0] = costs[0][:]
        
        for i in range(1, len(costs)):
            cost = costs[i]
            dp[i][0] = cost[0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = cost[1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = cost[2] + min(dp[i-1][0], dp[i-1][1])
            
        return min(dp[-1])
