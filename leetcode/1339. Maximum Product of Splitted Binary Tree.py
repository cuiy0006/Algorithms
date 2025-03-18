# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def getsum(node):
            if node is None:
                return 0
            return getsum(node.left)+getsum(node.right)+node.val
        total = getsum(root)

        res = 0
        def traverse(node):
            if node is None:
                return 0
            curr = node.val + traverse(node.left) + traverse(node.right)
            nonlocal res
            res = max(res, (total-curr)*curr)
            return curr
        traverse(root)
        return res % (10**9 + 7)
            
