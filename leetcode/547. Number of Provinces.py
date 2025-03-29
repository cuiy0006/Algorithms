class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = {city:city for city in range(n)}
        def find_ancestor(node):
            if parent[node] == node:
                return node
            parent[node] = find_ancestor(parent[node])
            return parent[node]
        
        for a in range(n):
            for b in range(a):
                if isConnected[a][b] == 1:
                    anc_a = find_ancestor(a)
                    anc_b = find_ancestor(b)
                    parent[anc_a] = anc_b

        s = set()
        for city in range(n):
            ancestor = find_ancestor(city)
            if ancestor not in s:
                s.add(ancestor)
        return len(s)



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False] * n
        
        def helper(city):
            if seen[city]:
                return
            
            seen[city] = True
            
            for other, connected in enumerate(isConnected[city]):
                if connected:
                    helper(other)
        
        res = 0
        for city in range(n):
            if seen[city]:
                continue
            res += 1
            helper(city)
        
        return res

    
    
    
 class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False] * n
        
        graph = defaultdict(list)
        for city in range(n):
            for other, connected in enumerate(isConnected[city]):
                if connected:
                    graph[city].append(other)


        def helper(city):
            if seen[city]:
                return
            
            seen[city] = True
            
            for other in graph[city]:
                helper(other)

        res = 0
        for city in range(n):
            if seen[city]:
                continue
            res += 1
            helper(city)
        
        return res
