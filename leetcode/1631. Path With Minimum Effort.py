from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        
        grid = [[sys.maxsize for i in range(n)] for j in range(m)]
        grid[0][0] = 0
        
        h = []
        heappush(h, (0, 0, 0))
        
        while len(h) != 0:
            diff, x, y = heappop(h)
            
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x0 = x + d[0]
                y0 = y + d[1]

                if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
                    continue
                max_diff = max(diff, abs(heights[x0][y0] - heights[x][y]))
                
                if max_diff < grid[x0][y0]:
                    grid[x0][y0] = max_diff
                    heappush(h, (max_diff, x0, y0))

        return grid[-1][-1]
