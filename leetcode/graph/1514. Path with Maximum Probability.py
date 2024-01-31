class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, [a, b] in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        h = [] # [(prob from start, node)]
        heappush(h, (-1, start_node))
        visited = {}

        while len(h) != 0:
            prob, node = heappop(h)
            prob = -prob
            if node in visited and prob <= visited[node]:
                continue
            visited[node] = prob
            for neighbor, p in graph[node]:
                heappush(h, (-p*prob, neighbor))
        
        if end_node not in visited:
            return 0
        return visited[end_node]

