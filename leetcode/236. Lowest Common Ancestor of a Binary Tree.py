# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node == None:
                return None
            if node == p or node == q:
                return node
            left = helper(node.left)
            right = helper(node.right)
            if (left == p and right == q) or (left == q and right == p):
                return node
            if left == None:
                return right
            if right == None:
                return left
            return None
        return helper(root)
