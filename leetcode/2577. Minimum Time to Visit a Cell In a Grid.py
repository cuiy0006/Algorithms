class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        cost = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        h = [(0, 0, 0)]
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        while len(h) != 0:
            c, x, y = heappop(h)
            if x == m-1 and y == n-1:
                return c
            if c >= cost[x][y]:
                continue
            cost[x][y] = c
            for d in dirs:
                x0 = x+d[0]
                y0 = y+d[1]
                if x0 < 0 or x0 > m-1 or y0 < 0 or y0 > n-1:
                    continue
                time = grid[x0][y0]
                if time > c:
                    if (time-c) % 2 == 0:
                        heappush(h, (time+1, x0, y0))
                    else:
                        heappush(h, (time, x0, y0))
                else:
                    heappush(h, (c+1, x0, y0))
        return -1 



