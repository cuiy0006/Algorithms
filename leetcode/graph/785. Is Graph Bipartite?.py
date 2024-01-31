class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}

        def traverse(node, tag):
            if node in visited:
                return visited[node] == tag

            visited[node] = tag
            for neighbor in graph[node]:
                if not traverse(neighbor, 1-tag):
                    return False
            return True

        for node in range(len(graph)):
            if node in visited:
                continue
            if not traverse(node, 0):
                return False
        return True

