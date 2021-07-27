class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        last = matrix[0]
        res = sum(last)
        
        for i in range(1, len(matrix)):
            curr = [0] * len(matrix[i])
            curr[0] = matrix[i][0]
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 1:
                    curr[j] = 1 + min(curr[j - 1], last[j - 1], last[j])
                else:
                    curr[j] = 0
            
            res += sum(curr)
            last = curr
        
        return res
        
