class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix) == 0:
            return []
        pacific = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        def findp(x, y, last):
            if x > len(matrix) - 1 or x < 0 or y > len(matrix[0]) - 1 or y < 0 or pacific[x][y] == 1:
                return
            
            if last is None or matrix[x][y] >= last:
                pacific[x][y] = True
                findp(x + 1, y, matrix[x][y])
                findp(x - 1, y, matrix[x][y])
                findp(x, y + 1, matrix[x][y])
                findp(x, y - 1, matrix[x][y])
                
                
        for i in range(len(matrix)):
            findp(i, 0, None)
            
        for i in range(len(matrix[0])):
            findp(0, i, None)
                  
        res = []
        atlantic = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        def finda(x, y, last):
            if x > len(matrix) - 1 or x < 0 or y > len(matrix[0]) - 1 or y < 0 or atlantic[x][y] == 1:
                return
            
            if last is None or matrix[x][y] >= last:
                atlantic[x][y] = True
                if pacific[x][y] and atlantic[x][y]:
                    res.append([x, y])
                finda(x + 1, y, matrix[x][y])
                finda(x - 1, y, matrix[x][y])
                finda(x, y + 1, matrix[x][y])
                finda(x, y - 1, matrix[x][y])
                
        for i in range(len(matrix)):
            finda(i, len(matrix[0]) - 1, None)
            
        for i in range(len(matrix[0])):
            finda(len(matrix) - 1, i, None)
            
        return res
