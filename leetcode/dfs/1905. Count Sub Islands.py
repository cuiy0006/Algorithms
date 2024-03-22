class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def traverse(x, y):
            if x < 0 or x > len(grid2)-1 or y < 0 or y > len(grid2[0])-1:
                return True
            if grid2[x][y] != 1:
                return True
            if grid1[x][y] != 1:
                return False
            grid2[x][y] = 2
            res1 = traverse(x+1, y)
            res2 = traverse(x-1, y)
            res3 = traverse(x, y+1)
            res4 = traverse(x, y-1)
            return res1 and res2 and res3 and res4
        
        cnt = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if traverse(i, j):
                        cnt += 1
        return cnt