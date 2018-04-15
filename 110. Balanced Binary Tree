# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node):
            if node is None:
                return (0, True)
            left, isbalance = helper(node.left)
            if not isbalance:
                return (-1, False)
            right, isbalance = helper(node.right)
            if not isbalance:
                return (-1, False)
            
            if abs(left - right) > 1:
                return (-1, False)
            return (max(left, right) + 1, True)
        
        _, isbalance = helper(root)
        return isbalance
