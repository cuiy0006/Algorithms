class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        
        for l in range(1,len(s)+1):
            i = 0
            while i + l <= len(s):
                j = i + l - 1
                if i == j:
                    dp[i+1][j+1] = 1
                    i += 1
                    continue
                
                if s[i] == s[j]:
                    dp[i+1][j+1] = dp[i+2][j] + 2
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i+2][j+1])
                i += 1

        return dp[1][len(s)]
