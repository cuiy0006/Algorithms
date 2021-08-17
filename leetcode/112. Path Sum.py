# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        
        def preorder(node, curr):
            if node is None:
                return False
            if node.left is None and node.right is None:
                if curr + node.val == targetSum:
                    return True
                else:
                    return False
            
            return preorder(node.left, curr + node.val) or preorder(node.right, curr + node.val)
            
        
        return preorder(root, 0)
