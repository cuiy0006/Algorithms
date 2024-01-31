class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for [a, b] in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = {}

        def traverse(node, tag):
            if node in visited:
                return visited[node] == tag

            visited[node] = tag
            for other in graph[node]:
                if not traverse(other, 1-tag):
                    return False
            return True

        for node in graph:
            if node in visited:
                continue
            if not traverse(node, 0):
                return False
        return True
