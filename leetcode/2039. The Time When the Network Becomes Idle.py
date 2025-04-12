class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        for [u, v] in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque([0])
        seen = set()
        d = 0
        res = -sys.maxsize
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node in seen:
                    continue
                seen.add(node)
                total = d*2
                if patience[node] >= total:
                    res = max(res, total+1)
                else:
                    start = total - total % patience[node]
                    if total % patience[node] == 0:
                        start -= patience[node]
                    res = max(res, start+total+1)
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        q.append(neighbor)
            d += 1
        return res


