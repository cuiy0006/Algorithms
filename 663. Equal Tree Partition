# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        def treeSum(node, s):
            if node == None:
                return 0
            total = node.val + treeSum(node.left, s) + treeSum(node.right, s)
            if node != root and total not in s:
                s.add(total)
            return total
        
        s = set()
        total = treeSum(root, s)
        half = total / 2
        return half in s
