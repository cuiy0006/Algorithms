class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        h = [(-1, start_node)]
        dic = {node:0 for node in range(n)}

        while len(h) != 0:
            prob, node = heappop(h)
            prob = -prob
            if prob <= dic[node]:
                continue
            dic[node] = prob
            if node == end_node:
                return prob
            if node not in graph:
                continue
            for neighbor, p in graph[node]:
                heappush(h, (-prob*p, neighbor))

        return dic[end_node]
