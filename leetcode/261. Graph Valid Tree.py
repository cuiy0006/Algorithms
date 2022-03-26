class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0 and n == 1:
            return True
        dic = {}
        for a, b in edges:
            if a not in dic:
                dic[a] = []
            if b not in dic:
                dic[b] = []
            
            dic[a].append(b)
            dic[b].append(a)
        
        
        def helper(curr, last, s):
            if curr in s:
                return False
            
            if curr not in dic:
                return False
            
            s.add(curr)
            
            for node in dic[curr]:
                if node == last:
                    continue
                    
                if not helper(node, curr, s):
                    return False
                
            return True
        
        s = set()
        res = helper(0, None, s)
        
        return res and len(s) == n
