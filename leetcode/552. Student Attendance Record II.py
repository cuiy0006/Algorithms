class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[0 for _ in range(6)] for _ in range(n)]
        dp[0][3] = 1
        dp[0][1] = 1
        dp[0][0] = 1
        
        for i in range(1, n):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 1000000007
            dp[i][1] = dp[i-1][0]
            dp[i][2] = dp[i-1][1]
            dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5]) % 1000000007
            dp[i][4] = dp[i-1][3]
            dp[i][5] = dp[i-1][4]
        
        return sum(dp[-1]) % 1000000007
        
        
#           a       l       p  
# a0l0    a1l0    a0l1     a0l0
# a0l1    a1l0    a0l2     a0l0
# a0l2    a1l0     x       a0l0
# a1l0     x      a1l1     a1l0
# a1l1     x      a1l2     a1l0
# a1l2     x        x      a1l0
