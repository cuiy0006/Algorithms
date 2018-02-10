class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left = 0
        right = n - 1
        for i in range(n//2):
            for j in range(left, right):
                x = i
                y = j
                tmp = matrix[x][y]
                for k in range(4):
                    matrix[y][n-x-1],tmp = tmp,matrix[y][n-x-1]
                    x, y = y, n-x-1
            left += 1
            right -= 1


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            left = 0
            right = n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
