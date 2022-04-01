class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        seen = set()
        graph = {}
        
        for [a, b] in edges:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
            
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
            
        def find_component(node):
            if node in seen:
                return
            
            seen.add(node)
            if node not in graph:
                return
            for neighbour in graph[node]:
                find_component(neighbour)
                
        
        for node in range(n):
            if node in seen:
                continue
            cnt += 1
            find_component(node)
        
        return cnt
        
