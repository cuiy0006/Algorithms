class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def is_valid(x, y):
            target = matrix[x][y]
            while x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]):
                if matrix[x][y] != target:
                    return False
                x += 1
                y += 1
            return True
        
        for x in range(0, len(matrix)):
            if not is_valid(x, 0):
                return False
        
        for y in range(1, len(matrix[0])):
            if not is_valid(0, y):
                return False
        return True
