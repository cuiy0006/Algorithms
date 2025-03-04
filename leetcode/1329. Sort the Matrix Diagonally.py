class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            x = i
            y = 0
            lst = []
            while x < m and y < n:
                lst.append(mat[x][y])
                x += 1
                y += 1
            lst.sort()
            idx = 0
            x = i
            y = 0
            while x < m and y < n:
                mat[x][y] = lst[idx]
                idx += 1
                x += 1
                y += 1
        
        for j in range(1, n):
            x = 0
            y = j
            lst = []
            while x < m and y < n:
                lst.append(mat[x][y])
                x += 1
                y += 1
            lst.sort()
            idx = 0
            x = 0
            y = j
            while x < m and y < n:
                mat[x][y] = lst[idx]
                idx += 1
                x += 1
                y += 1
        return mat
