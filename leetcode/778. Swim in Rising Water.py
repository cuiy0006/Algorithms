from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = -sys.maxsize
        
        h = []
        heappush(h, (grid[0][0], 0, 0))
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        while len(h) != 0:
            val, x, y = heappop(h)
            if visited[x][y]:
                continue
            visited[x][y] = True
            res = max(res, val)
            if x == len(grid)-1 and y == len(grid[0])-1:
                return res
            
            for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x0 = x+d[0]
                y0 = y+d[1]
                
                if x0 < 0 or x0 >= len(grid) or y0 < 0 or y0 >= len(grid[0]):
                    continue
                heappush(h, (grid[x0][y0], x0, y0))
        
        return res
            
            
