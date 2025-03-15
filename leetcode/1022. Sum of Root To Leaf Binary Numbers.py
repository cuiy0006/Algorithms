# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, curr):
            if node is None:
                return
            curr = curr*2+node.val
            if node.left is None and node.right is None:
                nonlocal res
                res += curr
            traverse(node.left, curr)
            traverse(node.right, curr)
        traverse(root, 0)
        return res
