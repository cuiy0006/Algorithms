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
