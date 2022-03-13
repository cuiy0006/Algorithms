class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = grid[0][:]
        
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = min([dp[i-1][k] for k in range(n) if k != j]) + grid[i][j]
        
        return min(dp[-1])
