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
