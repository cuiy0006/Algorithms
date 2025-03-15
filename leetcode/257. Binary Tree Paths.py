# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node, val):
            if node is None:
                return
            val += str(node.val)
            if node.left is None and node.right is None:
                nonlocal res
                res += int(val)
                return
            helper(node.left, val)
            helper(node.right, val)
        
        helper(root, '')
        return res
