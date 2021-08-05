class Solution:
    def numOfWays(self, n: int) -> int:
        dp = [[0, 0] for i in range(n)]
        dp[0][0] = 6
        dp[0][1] = 6
        
        MOD = 10 ** 9 + 7
        
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 1][1] * 2) % MOD
            dp[i][1] = (dp[i - 1][0] * 2 + dp[i - 1][1] * 3) % MOD
        
        return (dp[n-1][0] + dp[n-1][1]) % MOD
