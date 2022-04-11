from collections import deque
import sys
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[[sys.maxsize for _ in range(k+1)] for _ in range(n)] for _ in range(m)]
        
        q = deque([(0, 0, 0, -1)]) # (x, y, used, length) 
        
        while len(q) != 0:
            x, y, used, length = q.popleft()
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                continue
            
            if grid[x][y] == 1:
                if used == k:
                    continue
                else:
                    used += 1
            
            length += 1
            if dp[x][y][used] <= length:
                continue
                
            dp[x][y][used] = length
            if x == m - 1 and y == n - 1:
                return length
            
            for x0, y0 in direction:
                q.append((x+x0, y+y0, used, length))
            
        res = min(dp[-1][-1])
        if res == sys.maxsize:
            return -1
        else:
            return res
