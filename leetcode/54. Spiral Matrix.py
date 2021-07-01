class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d_i = 0
        x = 0
        y = 0
        res = [matrix[0][0]]
        total = len(matrix[0]) * len(matrix)
        
        while len(res) <  total:
            direction = directions[d_i]
            d_i = (d_i + 1) % 4
            while True:
                x0 = x + direction[0]
                y0 = y + direction[1]
                if y0 < left:
                    down -= 1
                    break
                if y0 > right:
                    up += 1
                    break
                if x0 < up:
                    left += 1
                    break
                if x0 > down:
                    right -= 1
                    break
                res.append(matrix[x0][y0])
                x = x0
                y = y0
        
        return res
            
            
            
