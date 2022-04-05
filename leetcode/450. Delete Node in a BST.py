# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        node = root
        parent = None
        while node is not None and node.val != key:
            parent = node
            if node.val > key:
                node = node.left
            else:
                node = node.right
        if node is None:
            return root

        if node.left is None and node.right is None:
            if parent is None:
                return None
            else:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
        
        elif node.left is not None:
            parent2 = node
            node2 = node.left
            while node2.right is not None:
                parent2 = node2
                node2 = node2.right
            if parent2 == node:
                node.left = node2.left
            else:
                parent2.right = node2.left
            node.val = node2.val
            
        elif node.right is not None:
            parent2 = node
            node2 = node.right
            while node2.left is not None:
                parent2 = node2
                node2 = node2.left
            if parent2 == node:
                node.right = node2.right
            else:
                parent2.left = node2.right
            node.val = node2.val
        return root
        
