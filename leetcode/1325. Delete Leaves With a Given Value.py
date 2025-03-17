# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete_node(node):
            if node is None:
                return True
            left = delete_node(node.left)
            right = delete_node(node.right)
            if left:
                node.left = None
            if right:
                node.right = None
            if left and right and node.val == target:
                return True
            return False
        
        if delete_node(root):
            return None
        return root
