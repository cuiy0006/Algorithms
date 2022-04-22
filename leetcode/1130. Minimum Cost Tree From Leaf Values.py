import sys

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        
        dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        
        # [i xxxxx k] [k+1 xxxx j]
        
        for i in range(n):
            dp[i][i] = 0
        
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i+l-1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], max(arr[i:k+1])*max(arr[k+1:j+1]) + dp[i][k] + dp[k+1][j])
        
        return dp[0][n-1]
