# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        curr = -sys.maxsize
        def inorder(node):
            if node is None:
                return True
            if not inorder(node.left):
                return False
            nonlocal curr
            if curr >= node.val:
                return False
            curr = node.val
            if not inorder(node.right):
                return False
            return True
        
        return inorder(root)
