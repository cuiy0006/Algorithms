class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        if m == 0:
            return 0
        n = len(M[0])
        res = 0
        
        dp = [[[0, 0, 0, 0] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                   continue
                dp[i][j] = [1,1,1,1]
                if i > 0:
                    dp[i][j][0] += dp[i - 1][j][0]
                if j > 0:
                    dp[i][j][1] += dp[i][j - 1][1]
                if i > 0 and j > 0:
                    dp[i][j][2] += dp[i - 1][j - 1][2]
                if i > 0 and j < n - 1:
                    dp[i][j][3] += dp[i - 1][j + 1][3]
                res = max(res, max(dp[i][j]))
                
        return res
                
                
