class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None for _ in range(n)] for _ in range(n)]

        directions = ((0,1),(1,0),(0,-1),(-1,0))
        left = 0
        right = n-1
        up = 0
        down = n-1

        d = 0
        x = 0
        y = 0
        curr = 2
        res[0][0] = 1
        while True:
            x0, y0 = directions[d]
            while x+x0 >= up and x+x0 <= down and y+y0 >= left and y+y0 <= right:
                x += x0
                y += y0
                res[x][y] = curr
                curr += 1      

            if d == 0:
                up += 1
            elif d == 1:
                right -= 1
            elif d == 2:
                down -= 1
            else:
                left += 1
            if left > right or up > down:
                break
            d = (d+1)%4
        
        return res
