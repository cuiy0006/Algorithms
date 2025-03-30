class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        dic = {}
        zeros = []
        res = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                if grid[i][j] > 1:
                    dic[(i, j)] = grid[i][j]-1
        
        def get_moves(idx):
            if idx == len(zeros):
                return 0
            x, y = zeros[idx]
            res = sys.maxsize
            for x0, y0 in dic.keys():
                if dic[(x0, y0)] == 0:
                    continue
                dic[(x0, y0)] -= 1
                res = min(res, abs(x-x0) + abs(y-y0) + get_moves(idx+1))
                dic[(x0, y0)] += 1
            return res
        return get_moves(0)
