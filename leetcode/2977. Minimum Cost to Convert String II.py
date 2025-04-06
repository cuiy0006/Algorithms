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
            dic = {}
            h = [(0, a)]
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

        original = set(original)
        changed = set(changed)
        lengths = set(len(word) for word in original)
        @cache
        def find_cost(idx):
            if idx >= len(source):
                return 0
            curr = sys.maxsize
            if source[idx] == target[idx]:
                curr = min(curr, find_cost(idx+1))
            for l in lengths:
                word1 = source[idx:idx+l]
                word2 = target[idx:idx+l]
                if word1 in original and word2 in changed:
                    d = distance(word1, word2)
                    if d == -1:
                        continue
                    curr = min(curr, d + find_cost(idx+l))
            return curr
        
        res = find_cost(0)
        return -1 if res == sys.maxsize else res
