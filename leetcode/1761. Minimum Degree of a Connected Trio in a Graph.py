class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        degree = defaultdict(int)
        
        for [x, y] in edges:
            graph[min(x, y)].add(max(x, y))
            degree[x] += 1
            degree[y] += 1
            
        min_degree = sys.maxsize
        
        for x in range(1, n+1):
            for y in graph[x]:
                curr = degree[x] + degree[y] - 6
                for z in graph[y]:
                    if z not in graph[x]:
                        continue
                        
                    min_degree = min(min_degree, curr + degree[z])
                    if min_degree == 0:
                        return 0
                    
        
        return min_degree if min_degree != sys.maxsize else -1
    
    
    
    
