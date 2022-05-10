# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def preorder(node, max_val):
            if node is None:
                return 0
            
            res = 0
            if max_val <= node.val:
                res += 1
                max_val = node.val
            
            res += preorder(node.left, max_val) + preorder(node.right, max_val)
        
            return res
        
        
        return preorder(root, -sys.maxsize)

            
