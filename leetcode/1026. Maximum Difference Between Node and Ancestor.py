# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, max_val, min_val):
            if node is None:
                return
            nonlocal res
            res = max(res, abs(max_val - node.val), abs(min_val - node.val))
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            traverse(node.left, max_val, min_val)
            traverse(node.right, max_val, min_val)

        traverse(root, root.val, root.val)
        return res

