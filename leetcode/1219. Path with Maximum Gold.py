class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        def get_gold(x, y):
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                return 0
            if grid[x][y] == 0:
                return 0
            val = grid[x][y]
            grid[x][y] = 0
            max_gold = 0
            for x0, y0 in dirs:
                max_gold = max(max_gold, get_gold(x+x0, y+y0))
            grid[x][y] = val
            return val + max_gold
        
        res = 0
        for x in range(m):
            for y in range(n):
                res = max(res, get_gold(x, y))
        return res
