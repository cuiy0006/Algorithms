# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        def helper(first, second):
            if first is None and second is None:
                return True
            if first is None and second is not None:
                return False
            if first is not None and second is None:
                return False
            if first.val != second.val:
                return False
            return helper(first.left, second.right) and helper(first.right, second.left)
        
        return helper(root.left, root.right)
