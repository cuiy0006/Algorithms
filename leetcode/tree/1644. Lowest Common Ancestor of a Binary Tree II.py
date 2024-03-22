# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node is None:
                return None, False
            left, left_is_ancestor = helper(node.left)
            right, right_is_ancestor = helper(node.right)
            if left_is_ancestor:
                return left, True
            if right_is_ancestor:
                return right, True
            if left is not None and right is not None:
                return node, True
            if left is not None or right is not None:
                if node == p or node == q:
                    return node, True
                else:
                    return node, False
            if node == p or node == q:
                return node, False
            else:
                return None, False
        
        ancestor, is_ancestor = helper(root)
        if is_ancestor:
            return ancestor
        else:
            return None
