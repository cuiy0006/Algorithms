class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def traverse(x, y):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return False
            if grid[x][y] != 0:
                return True
            grid[x][y] = 2
            res = True
            res1 = traverse(x+1, y)
            res2 = traverse(x-1, y)
            res3 = traverse(x, y+1)
            res4 = traverse(x, y-1)
            return res1 and res2 and res3 and res4
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if traverse(i, j):
                        cnt += 1
        return cnt