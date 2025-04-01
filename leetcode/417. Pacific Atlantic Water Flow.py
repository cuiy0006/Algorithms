class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        def get_pacific(x, y, last):
            if x < 0 or y < 0 or x > m-1 or y > n-1:
                return
            if heights[x][y] < last or pacific[x][y]:
                return
            pacific[x][y] = True
            for direction in dirs:
                get_pacific(x+direction[0], y+direction[1], heights[x][y])

        def get_atlantic(x, y, last):
            if x < 0 or y < 0 or x > m-1 or y > n-1:
                return
            if heights[x][y] < last or atlantic[x][y]:
                return
            atlantic[x][y] = True
            for direction in dirs:
                get_atlantic(x+direction[0], y+direction[1], heights[x][y])

        for i in range(m):
            get_pacific(i, 0, -sys.maxsize)
            get_atlantic(i, n-1, -sys.maxsize)
        for j in range(n):
            get_pacific(0, j, -sys.maxsize)
            get_atlantic(m-1, j, -sys.maxsize)

        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res
