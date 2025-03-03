class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        d = 0
        up = 0
        down = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        res = [matrix[0][0]]
        x, y = 0, 0
        while True:
            x0, y0 = directions[d]
            while x+x0 >= up and x+x0 <= down and y+y0 >= left and y+y0 <= right:
                x += x0
                y += y0
                res.append(matrix[x][y])
            if d == 0:
                up += 1
            elif d == 1:
                right -= 1
            elif d == 2:
                down -= 1
            else:
                left += 1
            if up > down or left > right:
                break
            d = (d+1) % 4
        return res
