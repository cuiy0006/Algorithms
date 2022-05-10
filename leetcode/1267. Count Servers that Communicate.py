class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        node_to_p = {}
        
        m = len(grid)
        n = len(grid[0])
        
        def find_ancestor(node):
            while node in node_to_p and node_to_p[node] != node:
                node = node_to_p[node]
            return node
        
        for i in range(m):
            servers = [(i, j) for j in range(n) if grid[i][j]==1]
            if len(servers) != 0:
                ancestor = find_ancestor(servers[0])
                node_to_p[servers[0]] = ancestor
                for k in range(1, len(servers)):
                    node_to_p[find_ancestor(servers[k])] = ancestor
        
        for j in range(n):
            servers = [(i, j) for i in range(m) if grid[i][j]==1]
            if len(servers) != 0:
                ancestor = find_ancestor(servers[0])
                node_to_p[servers[0]] = ancestor
                for k in range(1, len(servers)):
                    node_to_p[find_ancestor(servers[k])] = ancestor
        
        ancestor_to_cnt = defaultdict(int)
        for node in node_to_p:
            ancestor = find_ancestor(node)
            ancestor_to_cnt[ancestor] += 1
        
        res = sum((cnt for cnt in ancestor_to_cnt.values() if cnt != 1))
        return res




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
        
