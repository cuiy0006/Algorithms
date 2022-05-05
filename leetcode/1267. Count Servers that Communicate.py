class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        row_dic = defaultdict(list)
        col_dic = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_dic[i].append(j)
                    col_dic[j].append(i)
        
        def helper(x, y):
            if visited[x][y]:
                return 0
            
            visited[x][y] = True
            res = 1
            cols = row_dic[x]
            del row_dic[x]
            rows = col_dic[y]
            del col_dic[y]
            
            for y0 in cols:
                res += helper(x, y0)
                
            for x0 in rows:
                res += helper(x0, y)
            
            return res
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = helper(i, j)
                    if curr > 1:
                        res += curr
        return res
        
