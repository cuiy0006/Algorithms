class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        word1 = s
        word2 = s[::-1]
        
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)):
            dp[i+1][0] = i + 1
        
        for j in range(len(word2)):
            dp[0][j+1] = j + 1
        
        for i, c1 in enumerate(word1):
            for j, c2 in enumerate(word2):
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
        
        return dp[i+1][j+1] // 2 <= k
