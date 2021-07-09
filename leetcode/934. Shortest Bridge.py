from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque()
        
        def find_island(x, y):
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
                return
            
            if grid[x][y] != 1:
                return
            
            grid[x][y] = '#'
            q.append((x, y, 0))
            find_island(x + 1, y)
            find_island(x - 1, y)
            find_island(x, y + 1)
            find_island(x, y - 1)
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    find_island(i, j)
                    break
            else:
                continue
            break
            
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while len(q) != 0:
            x, y, curr = q.popleft()
            
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
                continue
            
            if grid[x][y] == 1:
                return curr - 1
            
            if not visited[x][y]:
                visited[x][y] = True
            else:
                continue
            
            for dx, dy in dirs:
                q.append((x + dx, y + dy, curr + 1))
                
