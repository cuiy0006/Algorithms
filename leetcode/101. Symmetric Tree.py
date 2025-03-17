# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node1, node2):
            if node1 is None and node2 is not None:
                return False
            if node1 is not None and node2 is None:
                return False
            if node1 is None and node2 is None:
                return True
            if node1.val != node2.val:
                return False
            return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
        if root is None:
            return True
        return is_mirror(root.left, root.right)

