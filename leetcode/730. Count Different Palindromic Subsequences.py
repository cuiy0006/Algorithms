class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        M = 10 ** 9 + 7
        
        after = [[sys.maxsize for _ in range(4)] for _ in range(n)]
        prev = [[-sys.maxsize for _ in range(4)] for _ in range(n)]
        
        for k in range(4):
            ch = chr(ord('a')+k)
            i = 0
            for j in range(n):
                if s[j] != ch:
                    continue
                while i <= j:
                    after[i][k] = j
                    i += 1
        
        for k in range(4):
            ch = chr(ord('a')+k)
            i = n-1
            for j in range(n-1, -1, -1):
                if s[j] != ch:
                    continue
                while i >= j:
                    prev[i][k] = j
                    i -= 1
                            
        for i in range(n):
            dp[i][i] = 1
        
        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                for k in range(4):
                    ch = chr(ord('a')+k)
                    
                    p = after[i][k]
                    q = prev[j][k]
                    
                    if p < q:
                        # any inner palindrome plus bb like bXXXXb
                        dp[i][j] += dp[p+1][q-1] + 1
                        
                    
                    if p <= j:
                        # if inner palindrome doesn't include b then, add b
                        # if inner palindrome include b like 
                        #       - b, then add bb,
                        #       - bb, then add bbb,
                        dp[i][j] += 1
                    
                    dp[i][j] %= M
        
        
        return dp[0][n-1]
                
        

        
        
# ixxxxxxj
# 1. if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] else: dp[i][j] = dp[i+1][j] + dp[i][j-1]   *not right


# dp[i][j]: number of different non-empty panlindrome subsequences in s[i:j+1]
# ixaxxxxaxj
#   |    |
#   i1   j1
# dp[i1][j1]: the most outer a,  no matter how many palindromes in [i1+1, j1-1], adding a pair of a, to make them unique again

# after[i][ch]: starting from i, the position of next ch
# prev[j][ch]: starting from j, the position of previous ch

# iXXaXaXXj
# iXXXaaXXj
# iXXXaXXj
