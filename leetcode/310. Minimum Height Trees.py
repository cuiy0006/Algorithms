class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        dic = defaultdict(list)
        degree = defaultdict(int)
        for [x, y] in edges:
            dic[x].append(y)
            dic[y].append(x)
            degree[x] += 1
            degree[y] += 1
        
        q = deque()
        for node, d in degree.items():
            if d == 1:
                q.append(node)

        removed = 0
        while len(q) != 0:
            if removed + 1 == n or removed + 2 == n:
                break
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                degree[node] -= 1
                removed += 1
                for child in dic[node]:
                    degree[child] -= 1
                    if degree[child] == 0:
                        return [child]
                    elif degree[child] == 1:
                        q.append(child)
        return list(q)
