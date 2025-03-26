class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = {node:node for node in range(n)}
        def find_ancestor(node):
            if parent[node] == node:
                return node
            parent[node] = find_ancestor(parent[node])
            return parent[node]

        for node in range(n):
            left = leftChild[node]
            right = rightChild[node]
            root = find_ancestor(node)
            if left != -1:
                if find_ancestor(left) == root or find_ancestor(left) != left:
                    return False
                parent[left] = root
            if right != -1:
                if find_ancestor(right) == root or find_ancestor(right) != right:
                    return False
                parent[right] = root

        root = find_ancestor(0)
        for node in range(1, n):
            if find_ancestor(node) != root:
                return False
        return True
