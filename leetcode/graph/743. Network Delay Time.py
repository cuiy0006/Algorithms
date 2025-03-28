class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist_to = {node:sys.maxsize for node in range(1, n+1)}
        dist_to[k] = 0

        graph = {}
        for orig, dest, cost in times:
            if orig not in graph:
                graph[orig] = []
            graph[orig].append((dest, cost))
        
        h = [(0, k)]
        while len(h) != 0:
            d, node = heappop(h)
            if node not in graph:
                continue
            for dest, cost in graph[node]:
                if d+cost < dist_to[dest]:
                    dist_to[dest] = d+cost
                    heappush(h, (dist_to[dest], dest))
        
        res = max(dist_to.values())
        if res == sys.maxsize:
            return -1
        return res
