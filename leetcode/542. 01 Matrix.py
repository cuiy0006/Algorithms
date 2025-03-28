class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        res = [[sys.maxsize for j in range(n)] for i in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
        
        d = 0
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if x < 0 or x > m-1 or y < 0 or y > n-1:
                    continue
                if res[x][y] != sys.maxsize:
                    continue
                res[x][y] = d
                for x0, y0 in directions:
                    q.append((x+x0, y+y0))
            d += 1

        return res
