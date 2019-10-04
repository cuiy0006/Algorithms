class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        seen = [[0 for i in range(n)] for j in range(m)]
        
        def helper(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if seen[i][j] == 1 or grid[i][j] == '0':
                return
            seen[i][j] = 1
            helper(i + 1, j)
            helper(i - 1, j)
            helper(i, j + 1)
            helper(i, j - 1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and seen[i][j] == 0:
                    res += 1
                    helper(i, j)
        return res
