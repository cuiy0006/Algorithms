from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = defaultdict(list)
        
        for [a, b] in edges:
            dic[a].append(b)
            dic[b].append(a)
        
        seen = set()
        def helper(node, last):
            if node in seen:
                return False
            
            seen.add(node)
            for child in dic[node]:
                if child == last:
                    continue
                if not helper(child, node):
                    return False
            return True

        if not helper(0, -1):
            return False
        
        return n == len(seen)
