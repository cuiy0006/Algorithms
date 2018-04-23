from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        distances = [[0 for i in range(n)] for j in range(m)]
        visited = [[0 for i in range(n)] for j in range(m)]
        building = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = deque([(i, j)])
                    height = 1
                    building += 1
                    while len(q) != 0:
                        cnt = len(q)
                        while cnt > 0:
                            x0, y0 = q.popleft()
                            for d in directions:
                                x = x0 + d[0]
                                y = y0 + d[1]
                                if x < 0 or y < 0 or x >= m or y >= n:
                                    continue
                                if grid[x][y] != 0 or visited[x][y] != building-1:
                                    continue
                                distances[x][y] += height
                                visited[x][y] += 1
                                q.append((x, y))
                            cnt -= 1
                        height += 1
                    
        min_distance = sys.maxsize
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and visited[i][j] == building:
                    min_distance = min(min_distance, distances[i][j])
        return min_distance if min_distance != sys.maxsize else -1
