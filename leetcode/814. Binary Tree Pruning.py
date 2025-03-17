# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def contain_one(node):
            if node is None:
                return False
            left = contain_one(node.left)
            right = contain_one(node.right)

            if not left:
                node.left = None
            if not right:
                node.right = None
            
            return (node.val == 1) or left or right
        
        if not contain_one(root):
            return None
        return root
