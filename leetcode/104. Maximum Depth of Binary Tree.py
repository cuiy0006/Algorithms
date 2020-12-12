# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def helper(node, depth):
            if node == None:
                return
            res[0] = max(depth, res[0])
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        helper(root, 1)
        return res[0]
