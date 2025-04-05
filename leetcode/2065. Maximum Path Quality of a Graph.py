class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for [a, b, time] in edges:
            graph[a].append((b, time))
            graph[b].append((a, time))
        
        max_value = 0
        def get_maxtime(node, onpath, rest, value):
            if onpath[node] == 0:
                value += values[node]
            onpath[node] += 1
            if node == 0:
                nonlocal max_value
                max_value = max(max_value, value)

            for child, cost in graph[node]:
                if rest < cost:
                    continue
                get_maxtime(child, onpath, rest-cost, value)

            onpath[node] -= 1
        
        get_maxtime(0, defaultdict(int), maxTime, 0)
        return max_value

