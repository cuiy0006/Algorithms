class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        s = set()
        
        def helper(k):
            if k in s:
                return 0
            
            s.add(k)
            
            for i in range(len(isConnected)):
                if isConnected[k][i] == 1:
                    helper(i)
            
            return 1
        
        cnt = 0
        for i in range(len(isConnected)):
           cnt += helper(i)
        
        return cnt
