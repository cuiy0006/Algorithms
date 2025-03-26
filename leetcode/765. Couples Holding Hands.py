class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)//2
        parents = {node:node for node in range(n)}
        def find_ancestor(node):
            if parents[node] == node:
                return node
            parents[node] = find_ancestor(parents[node])
            return parents[node]
        
        for i in range(0, len(row), 2):
            couple1 = row[i] // 2
            couple2 = row[i+1] // 2
            parents[find_ancestor(couple1)] = find_ancestor(couple2)
        
        s = set()
        for i in range(n):
            ancestor =  find_ancestor(i)
            if ancestor not in s:
                s.add(ancestor)
        
        return n - len(s)
