class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        start = (0, 0)
        end = (m-1, n-1)

        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        dic = {(i, j): sys.maxsize for i in range(m) for j in range(n)}
        h = [(0, 0, 0)]
        while len(h) != 0:
            effort, x, y = heappop(h)
            if effort >= dic[(x, y)]:
                continue
            dic[(x, y)] = effort
            if (x, y) == end:
                return effort
            for x0,y0 in dirs:
                x1 = x+x0
                y1 = y+y0
                if x1 < 0 or x1 > m-1 or y1 < 0 or y1 > n-1:
                    continue
                heappush(h, (max(effort, abs(heights[x][y]-heights[x1][y1])), x1, y1))
        
        return -1




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
