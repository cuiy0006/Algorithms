class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x_min = 0
        y_min = 0
        x_max = len(matrix)-1
        y_max = len(matrix[0])-1

        res = [matrix[0][0]]
        i = 0
        j = 0
        n = 0
        while x_max >= x_min and y_max >= y_min:
            # print(i, j, x_min, x_max, y_min, y_max)
            n = n % 4
            d = dirs[n]
            while True:
                i0 = i + d[0]
                j0 = j + d[1]
                if i0 >= x_min and i0 <= x_max and j0 >= y_min and j0 <= y_max:
                    i = i0
                    j = j0
                    res.append(matrix[i][j])
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
            n += 1
        return res