class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(x, y):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                return
            if grid[x][y] != '1':
                return
            grid[x][y] = '2'
            traverse(x+1, y)
            traverse(x-1, y)
            traverse(x, y+1)
            traverse(x, y-1)
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    traverse(i, j)
        return cnt
