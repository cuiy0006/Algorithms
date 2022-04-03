from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        a = set()
        b = set()
        
        for node in range(len(graph)):
            if node in a or node in b:
                continue
            
            q = deque([node])
            curr_set = a
            other_set = b
        
            while len(q) != 0:
                size = len(q)
                while size != 0:
                    size -= 1
                    node = q.popleft()
                    if node in curr_set:
                        continue
                    
                    if node in other_set:
                        return False
                    curr_set.add(node)
        
                    for child in graph[node]:
                        q.append(child)

                curr_set, other_set = other_set, curr_set
        
        return True
