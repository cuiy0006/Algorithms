class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        zero_cnt = 0
        m = len(grid)
        n = len(grid[0])
        x0 = None
        y0 = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zero_cnt += 1
                if grid[i][j] == 1:
                    x0 = i
                    y0 = j

        def find_path(x, y, cnt):
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                return 0
            if grid[x][y] == 2:
                return 1 if cnt == zero_cnt else 0
            if grid[x][y] == -1 or grid[x][y] == 1:
                return 0
            grid[x][y] = -1
            res = 0
            for d in dirs:
                res += find_path(x+d[0], y+d[1], cnt+1)
            grid[x][y] = 0
            return res
        
        res = 0
        for d in dirs:
            res += find_path(x0+d[0], y0+d[1], 0)
        return res

