from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        turn = 0
        while len(q) != 0:
            size = len(q)
            while size > 0:
                size -= 1
                x, y = q.popleft()
                
                for (x0, y0) in dirs:
                    x1 = x + x0
                    y1 = y + y0
                    
                    if x1 < 0 or x1 > len(grid) - 1 or y1 < 0 or y1 > len(grid[0]) - 1:
                        continue
                    
                    if grid[x1][y1] != 1:
                        continue
                    
                    fresh -= 1
                    grid[x1][y1] = 2
                    q.append((x1, y1))
            if len(q) != 0:
                turn += 1
        
        if fresh > 0:
            return -1
        
        return turn
