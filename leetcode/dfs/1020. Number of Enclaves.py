class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def traverse(x, y):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return (0, True)
            if grid[x][y] != 1:
                return (0, False)
            grid[x][y] = 2
            cnt1, ret1 = traverse(x+1, y)
            cnt2, ret2 = traverse(x-1, y)
            cnt3, ret3 = traverse(x, y+1)
            cnt4, ret4 = traverse(x, y-1)
            return (cnt1 + cnt2 + cnt3 + cnt4 + 1, ret1 or ret2 or ret3 or ret4)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cnt, ret = traverse(i, j)
                    if not ret:
                        res += cnt
        return res