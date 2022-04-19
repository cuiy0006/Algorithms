# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        def is_leaf(node):
            if node.left is None and node.right is None:
                return True
            else:
                return False
        
        if is_leaf(root):
            return [root.val]
        
        leaves = []
        def find_leaves(node):
            if node is None:
                return
            
            if is_leaf(node):
                leaves.append(node.val)
            find_leaves(node.left)
            find_leaves(node.right)
        
        find_leaves(root)

        left = []
        def find_left_boundary(node):
            if node is None:
                return
            if is_leaf(node):
                return
            left.append(node.val)
            if node.left is not None:
                find_left_boundary(node.left)
            else:
                find_left_boundary(node.right)
        
        find_left_boundary(root.left)
        
        right = []
        def find_right_boundary(node):
            if node is None:
                return
            if is_leaf(node):
                return
            right.append(node.val)
            if node.right is not None:
                find_right_boundary(node.right)
            else:
                find_right_boundary(node.left)
        
        find_right_boundary(root.right)
        right.reverse()
        
        return [root.val] + left + leaves + right

            
