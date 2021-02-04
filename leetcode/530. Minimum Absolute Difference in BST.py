# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        import sys
        min_val = sys.maxsize
        last = None
        def helper(node):
            if node == None:
                return
            nonlocal min_val
            nonlocal last

            helper(node.left)
            
            if last != None:
                min_val = min(min_val, node.val - last.val)
            last = node
            helper(node.right)
            
        helper(root)
        return min_val
