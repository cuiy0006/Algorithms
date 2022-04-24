from collections import deque

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        q = deque([(len(grid)-1, len(grid[0])-1)])
        
        res = 0
        
        while len(q) != 0:
            x, y = q.popleft()
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                continue
            
            if grid[x][y] < 0:
                res += 1
                q.append((x-1,y))
                q.append((x,y-1))
                grid[x][y] = 0
        
        return res
