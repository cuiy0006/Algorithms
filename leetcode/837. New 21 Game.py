class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k - 1 + maxPts <= n:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        
        total = 0
        
        for i in range(n):
            if i < k:
                total += dp[i]
            if i >= maxPts:
                total -= dp[i - maxPts]
            
            dp[i + 1] = total / maxPts

        res = 0
        for i in range(k, n + 1):
            res += dp[i]
        return res
