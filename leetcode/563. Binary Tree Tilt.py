# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node is None:
                return (0, 0)
            lefttilt, leftsum = helper(node.left)
            righttilt, rightsum = helper(node.right)
            tilt = abs(leftsum-rightsum)
            return (lefttilt+righttilt+tilt, leftsum+rightsum+node.val)
        return helper(root)[0]
