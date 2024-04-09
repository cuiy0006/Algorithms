class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        q = deque([(0, 0)])
        d = 1
        seen = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if x == len(grid)-1 and y == len(grid[0])-1:
                    return d
                if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                    continue
                if grid[x][y] != 0:
                    continue
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                for x0, y0 in dirs:
                    q.append((x+x0, y+y0))
            d += 1
        return -1
