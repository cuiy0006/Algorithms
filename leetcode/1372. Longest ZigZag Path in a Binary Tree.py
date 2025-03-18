# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node):
            if node is None:
                return 0, 0
            ll, lr = traverse(node.left)
            rl, rr = traverse(node.right)
            nonlocal res
            res = max(res, lr+1, rl+1)
            return lr+1, rl+1
        traverse(root)
        return res-1

