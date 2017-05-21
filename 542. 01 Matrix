from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        res = [[sys.maxsize for j in range(n)] for j in range(m)]
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))
        
        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(q) != 0:
            x,y = q.popleft()
            for d in ds:
                x0 = x + d[0]
                y0 = y + d[1]
                if x0 < 0 or y0 < 0 or x0 > m - 1 or y0 > n - 1 or res[x0][y0] <= res[x][y] + 1:
                    continue
                res[x0][y0] = res[x][y] + 1
                q.append((x0, y0))
        return res
            
