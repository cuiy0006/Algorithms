class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def traverse(x, y, d, dirs):
            if x < 0 or x > len(grid)-1 or y < 0 or y > len(grid[0])-1:
                dirs.append(d + '0')
                return
            if grid[x][y] != 1:
                dirs.append(d + '0')
                return
            grid[x][y] = 2
            dirs.append(d + '1')
            traverse(x+1, y, 'd', dirs)
            traverse(x-1, y, 'u', dirs)
            traverse(x, y+1, 'r', dirs)
            traverse(x, y-1, 'l', dirs)
        
        seen = set()
        dirs = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    traverse(i, j, '', dirs)
                    dirs_str = ''.join(dirs)
                    if dirs_str not in seen:
                        seen.add(dirs_str)
                    dirs.clear()
        return len(seen)