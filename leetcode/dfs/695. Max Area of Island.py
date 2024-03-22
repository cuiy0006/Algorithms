class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def traverse(x, y):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return 0
            if grid[x][y] != 1:
                return 0
            grid[x][y] = 2
            area = 1
            area += traverse(x+1, y)
            area += traverse(x-1, y)
            area += traverse(x, y+1)
            area += traverse(x, y-1)
            return area
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, traverse(i, j))
        return res