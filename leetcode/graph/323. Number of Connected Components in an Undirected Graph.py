class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}

        for node in range(n):
            parent[node] = node
        
        def find_root(node):
            if parent[node] == node:
                return node
            parent[node] = find_root(parent[node])
            return parent[node]
        
        for [a, b] in edges:
            a_root = find_root(a)
            b_root = find_root(b)
            parent[a_root] = b_root

        roots = set()
        for node in range(n):
            root = find_root(node)
            if root not in roots:
                roots.add(root)
        return len(roots)
