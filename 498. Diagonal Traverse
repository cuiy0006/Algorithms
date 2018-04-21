class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        up = True
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []
        i = 0
        x = y = 0
        while i < m * n:
            res.append(matrix[x][y])
            if up:
                if y == n - 1:
                    x += 1
                    up = False
                elif x == 0:
                    y += 1
                    up = False
                else:
                    x -= 1
                    y += 1
            else:
                if x == m - 1:
                    y += 1
                    up = True
                elif y == 0:
                    x += 1
                    up = True
                else:
                    x += 1
                    y -= 1
            i += 1
        return res
