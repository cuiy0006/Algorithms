class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        
        for i in range(1, len(s)+1):
            dp[0][i] = i
            dp[i][0] = i
            
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
        
        return dp[-1][-1] // 2
        
