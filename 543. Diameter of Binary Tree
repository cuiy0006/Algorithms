# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node == None:
                return (0, 0)
            left_maxdepth, left_maxlength = helper(node.left)
            right_maxdepth, right_maxlength = helper(node.right)
            return (max(left_maxdepth, right_maxdepth) + 1, max(left_maxdepth+right_maxdepth, left_maxlength, right_maxlength))
        
        return helper(root)[1]
