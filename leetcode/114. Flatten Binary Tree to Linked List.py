# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.helper(root)
        
    def helper(self, node):
        if node is None:
            return
        
        self.helper(node.right)
        self.helper(node.left)
        
        node.right = self.prev
        node.left = None
        self.prev = node
