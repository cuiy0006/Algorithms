class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = {}
        for i in range(len(original)):
            a = original[i]
            b = changed[i]
            c = cost[i]
            if a not in graph:
                graph[a] = {}
            if b not in graph[a]:
                graph[a][b] = sys.maxsize
            graph[a][b] = min(graph[a][b], c)
        
        @cache
        def distance(a, b):
            h = [(0, a)]
            dic = {}
            while len(h) != 0:
                d, node = heappop(h)
                if node == b:
                    return d
                if node not in dic or dic[node] > d:
                    dic[node] = d
                    if node not in graph:
                        continue
                    for child, cost in graph[node].items():
                        heappush(h, (d+cost, child))
            return -1
        
        res = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                d = distance(source[i], target[i])
                if d == -1:
                    return -1
                res += d
        return res
