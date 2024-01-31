class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x:x[2])
        parent = {node:node for node in range(1, n+1)}

        def find_root(node):
            if parent[node] == node:
                return node
            parent[node] = find_root(parent[node])
            return parent[node]

        total = 0
        for [x, y, cost] in connections:
            x_root = find_root(x)
            y_root = find_root(y)
            if x_root != y_root:
                total += cost
                parent[x_root] = y_root
        
        root = find_root(1)
        for node in range(2, n+1):
            if root != find_root(node):
                return -1

        return total
