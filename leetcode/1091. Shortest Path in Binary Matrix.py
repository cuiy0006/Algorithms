from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        dp = [[-1 for i in range(len(grid[j]))] for j in range(len(grid))]
        
        q = deque([(0, 0)])
        length = 1
        
        while len(q) != 0:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                if dp[x][y] != -1:
                    continue
                dp[x][y] = length
                for x0, y0 in dirs:
                    x1 = x + x0
                    y1 = y + y0
                    if x1 < 0 or y1 < 0 or x1 > len(grid) - 1 or y1 > len(grid[0]) - 1:
                        continue
                    if grid[x1][y1] == 1:
                        continue
                    q.append((x1, y1))
                    grid[x1][y1] = 1
            length += 1

        return dp[-1][-1]
