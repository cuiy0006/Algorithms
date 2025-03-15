# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = -sys.maxsize
        def inorder(root):
            if root is None:
                return True
            if not inorder(root.left):
                return False
            nonlocal last
            if root.val <= last:
                return False
            last = root.val
            if not inorder(root.right):
                return False
            return True
        return inorder(root)

