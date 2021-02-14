class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + helper(i - 1, j) + helper(i + 1, j) + helper(i, j - 1) + helper(i, j + 1)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, helper(i, j))
        return res
