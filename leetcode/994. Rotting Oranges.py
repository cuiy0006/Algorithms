class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        seen = set()
        d = 0
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if x < 0 or x > m-1 or y < 0 or y > n-1 or grid[x][y] == 0:
                    continue
                if (x, y) in seen:
                    continue
                seen.add((x, y))
                if grid[x][y] == 1:
                    fresh -= 1
                for x0,y0 in directions:
                    q.append((x+x0, y+y0))
            if fresh == 0:
                break
            d += 1
        
        if fresh != 0:
            return -1
        return d
