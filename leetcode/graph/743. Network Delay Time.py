class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for [u, v, w] in times:
            graph[u].append((v, w))

        h = [] # time from k, node
        heappush(h, (0, k))
        visited = {}

        while len(h) != 0:
            time_from_k, node = heappop(h)
            if node in visited and visited[node] <= time_from_k:
                continue
            visited[node] = time_from_k
            for neighbor, time in graph[node]:
                heappush(h, (time_from_k + time, neighbor))
        
        if len(visited) != n:
            return -1
        return max(visited.values())
