from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        dic = defaultdict(list)
        degree = [0] * n
        
        for [a, b] in edges:
            dic[a].append(b)
            dic[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        q = deque()
        for i, d in enumerate(degree):
            if d == 1:
                q.append(i)
        
        removed = 0
        while True:
            if removed + 1 == n or removed + 2 == n:
                break
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                degree[node] = 0
                removed += 1
                for neighbour in dic[node]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        q.append(neighbour)

        return list(q)
                
        
