class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        ones = sum(sum(row) for row in mat)
        if ones == 0:
            return 0
        m = len(mat)
        n = len(mat[0])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def flip(x, y):
            reduced_ones = 0
            if mat[x][y] == 1:
                reduced_ones += 1
                mat[x][y] = 0
            else:
                reduced_ones -= 1
                mat[x][y] = 1

            for x0, y0 in directions:
                x1, y1 = x + x0, y + y0
                if x1 < 0 or x1 > m - 1 or y1 < 0 or y1 > n - 1:
                    continue
                if mat[x1][y1] == 1:
                    reduced_ones += 1
                    mat[x1][y1] = 0
                else:
                    reduced_ones -= 1
                    mat[x1][y1] = 1
            return reduced_ones

        
        def helper(idx, ones, flip_cnt):
            if idx == m * n:
                return -1
            
            cnt1 = helper(idx+1, ones, flip_cnt)

            x = idx // n
            y = idx % n

            ones -= flip(x, y)
            if ones == 0:
                flip(x, y)
                return flip_cnt+1
            else:
                cnt2 = helper(idx+1, ones, flip_cnt+1)
                flip(x, y)

            if cnt1 == -1 and cnt2 == -1:
                return -1
            elif cnt1 == -1:
                return cnt2
            elif cnt2 == -1:
                return cnt1
            else:
                return min(cnt1, cnt2)

        return helper(0, ones, 0)
