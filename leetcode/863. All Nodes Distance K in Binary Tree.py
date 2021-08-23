# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def preorder(node, parent):
            if node is None:
                return
            
            node.parent = parent
            preorder(node.left, node)
            preorder(node.right, node)
        
        preorder(root, None)
        res = []
        
        def find_nodes(node, distance, visited):
            if node is None or node in visited:
                return
            
            visited.add(node)
            if distance == k:
                res.append(node.val)
                return
            
            find_nodes(node.left, distance + 1, visited)
            find_nodes(node.right, distance + 1, visited)
            find_nodes(node.parent, distance + 1, visited)
            
        find_nodes(target, 0, set())
        return res
