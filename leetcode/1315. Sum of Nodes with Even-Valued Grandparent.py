# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, p_even, gp_even):
            if node is None:
                return
            if gp_even:
                nonlocal res
                res += node.val
            traverse(node.left, node.val%2==0, p_even)
            traverse(node.right, node.val%2==0, p_even)
        
        traverse(root, False, False)
        return res

