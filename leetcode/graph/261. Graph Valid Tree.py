class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {node:node for node in range(n)}
        def find_root(node):
            if parent[node] == node:
                return node
            parent[node] = find_root(parent[node])
            return parent[node]
        
        for [x, y] in edges:
            x_root = find_root(x)
            y_root = find_root(y)
            if x_root == y_root:
                return False
            parent[x_root] = y_root
        
        root = find_root(0)
        for node in range(1, n):
            if root != find_root(node):
                return False
        return True

