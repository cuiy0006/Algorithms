# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, isLeft):
            if node == None:
                return 0
            if node.left == None and node.right == None and isLeft:
                return node.val
            res = 0
            if node.left != None:
                res += helper(node.left, True)
            if node.right != None:
                res += helper(node.right, False)
            return res
        if root == None:
            return 0
        return helper(root, False)
