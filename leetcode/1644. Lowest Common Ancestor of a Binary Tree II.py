# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        seen = 0

        def helper(node):
            if node is None:
                return None
            
            if node == p or node == q:
                nonlocal seen
                seen += 1

            left = helper(node.left)
            right = helper(node.right)
            if node == p or node == q:
                return node
            
            if left is not None and right is not None:
                return node
            elif left is not None:
                return left
            elif right is not None:
                return right
            else:
                return None
            
        res = helper(root)
        if seen != 2:
            return None
        return res
