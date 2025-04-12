class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        res = []
        for j in range(n):
            max_width = 0
            for i in range(m):
                max_width = max(max_width, len(str(grid[i][j])))
            res.append(max_width)
        return res
