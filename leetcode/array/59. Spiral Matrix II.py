class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        matrix[0][0] = 1
        x_min = 0
        y_min = 0
        x_max = n-1
        y_max = n-1

        i = 0
        j = 0
        n = 0
        curr = 2
        while x_min <= x_max and y_min <= y_max:
            d = dirs[n]
            while True:
                i0 = i + d[0]
                j0 = j + d[1]
                if i0 >= x_min and i0 <= x_max and j0 >= y_min and j0 <= y_max:
                    i = i0
                    j = j0
                    matrix[i][j] = curr
                    curr += 1
                else:
                    break
            if n == 0:
                x_min += 1
            elif n == 1:
                y_max -= 1
            elif n == 2:
                x_max -= 1
            else:
                y_min += 1
            n = (n + 1) % 4
        return matrix
