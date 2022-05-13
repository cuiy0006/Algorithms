class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        maxlen = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    maxlen = max(maxlen, dp[i][j])
        return maxlen ** 2

    
    
    
    
    
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        edge = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if dp[i+1][j] == 0 and dp[i][j+1] == 0:
                    dp[i+1][j+1] = 1
                elif dp[i+1][j] ==  dp[i][j+1]:
                    dp[i+1][j+1] = dp[i+1][j]
                    if dp[i][j] >= dp[i][j+1]:
                        dp[i+1][j+1] += 1
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
                edge = max(edge, dp[i+1][j+1])
        
        return edge * edge
