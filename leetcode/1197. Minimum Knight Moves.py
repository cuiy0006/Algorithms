from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        
        q = deque([(0, 0)])
        visited = set()
        
        res = sys.maxsize
        step = 0
        while len(q) != 0:
            size = len(q)

            for _ in range(size):
                x1, y1 = q.popleft()
                if (x1, y1) == (x, y):
                    return step
                for x0, y0 in directions:
                    x2 = x1 + x0
                    y2 = y1 + y0
                    if (x2, y2) in visited:
                        continue
                    visited.add((x2, y2))
                    q.append((x2, y2))
            step += 1
            
        return -1
      
      
      

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        @cache
        def dfs(x, y):
            if (x, y) == (0, 0):
                return 0
            if (x, y) in ((0, 2), (2, 0), (1, 1)):
                return 2
            
            return min(dfs(abs(x-2), abs(y-1)), dfs(abs(x-1), abs(y-2))) + 1
            
        return dfs(abs(x), abs(y))
