class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def get_area(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                return 0
            
            if grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            area = 1
            area += get_area(x + 1, y)
            area += get_area(x - 1, y)
            area += get_area(x, y + 1)
            area += get_area(x, y - 1)
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, get_area(i, j))
        
        return max_area
