import sys
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        distances = [[-1 for i in range(n)] for j in range(m)]
        def helper(x, y, last):
            if x < 0 or y < 0 or x >= m or y >= n or last >= matrix[x][y]:
                return 0
            if distances[x][y] != -1:
                return distances[x][y]
            
            left = helper(x - 1, y, matrix[x][y])
            right = helper(x + 1, y, matrix[x][y])
            up = helper(x, y - 1, matrix[x][y])
            down = helper(x, y + 1, matrix[x][y])
            distances[x][y] = 1 + max(left, right, up, down)
            return distances[x][y]
        
        res = 0
        for i in range(m):
            for j in range(n):
                tmp = helper(i, j, -sys.maxsize)
                res = max(res, tmp)
        return res
