# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_sub(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            return is_sub(node1.left, node2.left) and is_sub(node1.right, node2.right)
        
        def preorder(node):
            if node is None:
                return False
            
            if is_sub(node, subRoot):
                return True
            
            return preorder(node.left) or preorder(node.right)
        
        return preorder(root)
            
