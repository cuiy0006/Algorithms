from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        total = 0
        
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    total += 1
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while len(q) != 0:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()
                for d in dirs:
                    x0, y0 = x + d[0], y + d[1]
                    if x0 < 0 or y0 < 0 or x0 > len(grid) - 1 or y0 > len(grid[0]) - 1:
                        continue
                    
                    if grid[x0][y0] == 1:
                        grid[x0][y0] = 2
                        total -= 1
                        q.append((x0, y0))
            if len(q) == 0:
                break
            
            minute += 1
        
        if total != 0:
            return -1
        else:
            return minute
