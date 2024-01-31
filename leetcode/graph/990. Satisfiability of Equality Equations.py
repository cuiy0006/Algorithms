class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        def find_root(node):
            if node == parent[node]:
                return node
            parent[node] = find_root(parent[node])
            return parent[node]
        
        for equation in equations:
            parent[equation[0]] = equation[0]
            parent[equation[3]] = equation[3]

        for equation in equations:
            if equation[1] == '=':
                a_root = find_root(equation[0])
                b_root = find_root(equation[3])
                parent[a_root] = b_root
        
        for equation in equations:
            if equation[1] == '!':
                a_root = find_root(equation[0])
                b_root = find_root(equation[3])
                if a_root == b_root:
                    return False
        return True

