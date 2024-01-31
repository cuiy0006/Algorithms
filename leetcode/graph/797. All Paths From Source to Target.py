class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        on_path = []
        visited = set()
        res = []

        def traverse(node):
            if node in visited:
                return

            on_path.append(node)
            visited.add(node)
            if node == len(graph) - 1:
                res.append(on_path[:])
            else:
                for neighbour in graph[node]:
                    traverse(neighbour)

            on_path.pop()
            visited.remove(node)
        
        traverse(0)
        return res
