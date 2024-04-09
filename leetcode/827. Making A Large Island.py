class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        area = {}
        idx = 2
        def helper(x, y, idx):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return 0
            if grid[x][y] != 1:
                return 0
            grid[x][y] = idx
            cnt = 1
            for x0, y0 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                cnt += helper(x+x0, y+y0, idx)
            return cnt

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                cnt = helper(x, y, idx)
                area[idx] = cnt
                idx += 1

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                cnt = 0 if grid[x][y] != 0 else 1
                seen = set()
                for x0, y0 in [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]:
                    x1 = x + x0
                    y1 = y + y0
                    if x1 < 0 or x1 > len(grid)-1 or y1 < 0 or y1 > len(grid[0])-1:
                        continue
                    if grid[x1][y1] in area and grid[x1][y1] not in seen:
                        cnt += area[grid[x1][y1]]
                        seen.add(grid[x1][y1])
                res = max(res, cnt)
        return res

