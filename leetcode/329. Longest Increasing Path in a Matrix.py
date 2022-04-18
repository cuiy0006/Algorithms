class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        def get_path(x, y, last):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                return 0
            if last is not None and last >= matrix[x][y]:
                return 0
            
            if dp[x][y] != -1:
                return dp[x][y]
            
            for (x0, y0) in directions:
                dp[x][y] = max(dp[x][y], get_path(x+x0, y+y0, matrix[x][y]) + 1)
            return dp[x][y]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, get_path(i, j, None))
        return res
