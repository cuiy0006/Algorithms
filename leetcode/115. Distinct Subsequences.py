class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        
        for i in range(len(s)):
            for j in range(min(i+1, len(t))):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        
        # print(dp)
        return dp[-1][-1]
        
