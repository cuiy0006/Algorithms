class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        degree = defaultdict(int)
        dic = defaultdict(list)
        for [a, b] in edges:
            degree[a] += 1
            degree[b] += 1
            dic[a].append(b)
            dic[b].append(a)
        
        q = deque()
        for node, d in degree.items():
            if d == 1:
                q.append(node)
        
        seen = set()
        while len(q) != 0:
            node = q.popleft()
            seen.add(node)
            for child in dic[node]:
                if child in seen:
                    continue
                degree[child] -= 1
                if degree[child] == 1:
                    q.append(child)
        
        s = set()
        for node, d in degree.items():
            if d > 1:
                s.add(node)
        for i in range(len(edges)-1, -1, -1):
            if edges[i][0] in s and edges[i][1] in s:
                return edges[i]
        return []
