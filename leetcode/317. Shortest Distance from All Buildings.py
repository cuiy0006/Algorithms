from collections import deque
import sys

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        locations = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        cnt = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    q = deque()
                    for d in directions:
                        q.append((x+d[0], y+d[1]))
                    
                    distance = 1
                    while len(q) != 0:
                        size = len(q)
                        for _ in range(size):
                            x0, y0 = q.popleft()
                            if x0 < 0 or x0 > len(grid)-1 or y0 < 0 or y0 > len(grid[0])-1:
                                continue
                            if grid[x0][y0] != cnt:
                                continue
                            grid[x0][y0] -= 1
                            
                            for d in directions:
                                q.append((x0+d[0], y0+d[1]))

                            locations[x0][y0] += distance
                            
                        distance += 1
                    cnt -= 1

        res = sys.maxsize
        for i in range(len(locations)):
            for j in range(len(locations[0])):
                if grid[i][j] == cnt:
                    res = min(res, locations[i][j])
        
        
        if res == sys.maxsize:
            return -1
        else:
            return res
                
