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
                    q.append((x, y))
                    
                    distance = 0
                    while len(q) != 0:
                        size = len(q)
                        for _ in range(size):
                            x0, y0 = q.popleft()
                            for d in directions:
                                x1, y1 = x0+d[0], y0+d[1]
                                if x1 < 0 or x1 > len(grid)-1 or y1 < 0 or y1 > len(grid[0])-1:
                                    continue
                                if grid[x1][y1] != cnt:
                                    continue
                                grid[x1][y1] -= 1
                                q.append((x1, y1))

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
                
