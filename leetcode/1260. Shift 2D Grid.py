class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        cnt = m*n
        k = k % cnt

        res = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i*n + j
                new_idx = (idx + k) % cnt
                new_i = new_idx // n
                new_j = new_idx % n
                res[new_i][new_j] = grid[i][j]
        
        return res
