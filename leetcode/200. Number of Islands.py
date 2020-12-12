#DFS
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        direction = [[0,1], [0,-1], [1,0], [-1,0]]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        def helper(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if not visited[i][j] and grid[i][j] == '1':
                visited[i][j] = True
                for x0, y0 in direction:
                    helper(i + x0, j + y0)
                return 1
            else:
                return 0
            
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt += helper(i, j)
        return cnt

#BFS

from collections import deque
D = ((0,1), (0,-1), (1,0), (-1,0))
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    visited[i][j] = True
                    q = deque([(i,j)])
                    while len(q) != 0:
                        x, y = q.popleft()
                        for d in D:
                            x0, y0 = x + d[0], y + d[1]
                            if x0 < 0 or x0 >= len(grid) or y0 < 0 or y0 >= len(grid[0]) or visited[x0][y0] or grid[x0][y0] == '0':
                                continue
                            visited[x0][y0] = True
                            q.append((x0, y0))
        return cnt
