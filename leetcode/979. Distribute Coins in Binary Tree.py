# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node):
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            nonlocal res
            res += abs(left) + abs(right)
            return left + right + node.val - 1
        traverse(root)
        return res
