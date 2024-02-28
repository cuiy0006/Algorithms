class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(n):
            l = 0
            r = n-1
            while l < r:
                matrix[l][j], matrix[r][j] = matrix[r][j], matrix[l][j]
                l += 1
                r -= 1
        
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
