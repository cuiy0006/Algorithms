class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def traverse(x, y, origin_x, origin_y, curr):
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                return
            if grid[x][y] == 0:
                return
            if visited[x][y]:
                return
            visited[x][y] = True
            curr.append((x-origin_x, y-origin_y))
            for d1,d2 in dirs:
                traverse(x+d1, y+d2, origin_x, origin_y, curr)
        
        s = set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and not visited[x][y]:
                    curr = []
                    traverse(x, y, x, y, curr)
                    h = tuple(curr)
                    if h not in s:
                        s.add(h)
        return len(s)



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
