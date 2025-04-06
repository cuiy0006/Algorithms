class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        res = 0
        for mask in range(2 ** n):
            graph = [[sys.maxsize for _ in range(n)] for _ in range(n)]
            for [a, b, d] in roads:
                if (mask >> a) & 1 == 0 or (mask >> b) & 1 == 0:
                    continue
                graph[a][b] = min(graph[a][b], d)
                graph[b][a] = min(graph[b][a], d)
            for i in range(n):
                graph[i][i] = 0
            
            for k in range(n):
                if (mask >> k) & 1 == 0:
                    continue
                for i in range(n):
                    if (mask >> i) & 1 == 0:
                        continue
                    for j in range(n):
                        if (mask >> j) & 1 == 0:
                            continue
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
            add = 1
            for i in range(n):
                for j in range(n):
                    if (mask >> i) & 1 == 0 or (mask >> j) & 1 == 0:
                        continue
                    if graph[i][j] > maxDistance:
                        add = 0
                if add == 0:
                    break 
            res += add
        return res
                        

