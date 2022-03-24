class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        dp = [[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        
        for i in range(len(s1)+1):
            dp[i][0] = 0
        
        for i in range(len(s1)):
            for j in range(min(i+1, len(s2))):
                if s1[i] == s2[j]:
                    if dp[i][j] == -1:
                        dp[i+1][j+1] = -1
                    else:
                        dp[i+1][j+1] = dp[i][j] + 1
                else:
                    if dp[i][j+1] == -1:
                        dp[i+1][j+1] = -1
                    else:
                        dp[i+1][j+1] = dp[i][j+1] + 1
                        
                if j == len(s2) - 1 and dp[i+1][j+1] == len(s2):
                    break
                  
        min_i = 0
        min_len = len(s1)
        j = len(s2) - 1
        for i in range(len(s1)):
            if dp[i+1][j+1] >= len(s2) and dp[i+1][j+1] < min_len:
                min_len = dp[i+1][j+1]
                min_i = i
        
        
        return s1[min_i-min_len+1:min_i+1]
