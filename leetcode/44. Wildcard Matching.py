class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        
        for i in range(len(p)):
            if p[i] == '*':
                dp[0][i+1] = dp[0][i]
        
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j] and s[i] == p[j]
        return dp[-1][-1]
