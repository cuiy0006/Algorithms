class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        m = len(matrix)
        n = len(matrix[0])
        path = [[-1 for _ in range(n)] for _ in range(m)]

        def traverse(x, y):
            if path[x][y] != -1:
                return path[x][y]
            path[x][y] = 1
            for x0, y0 in dirs:
                x1 = x0+x
                y1 = y0+y
                if x1 < 0 or x1 > m-1 or y1 < 0 or y1 > n-1:
                    continue
                if matrix[x1][y1] >= matrix[x][y]:
                    continue
                path[x][y] = max(path[x][y], traverse(x1, y1)+1)
            return path[x][y]
        
        for i in range(m):
            for j in range(n):
                traverse(i, j)

        return max([max(row) for row in path])


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        def get_path(x, y, last):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                return 0
            if last is not None and last >= matrix[x][y]:
                return 0
            
            if dp[x][y] != -1:
                return dp[x][y]
            
            for (x0, y0) in directions:
                dp[x][y] = max(dp[x][y], get_path(x+x0, y+y0, matrix[x][y]) + 1)
            return dp[x][y]
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, get_path(i, j, None))
        return res
