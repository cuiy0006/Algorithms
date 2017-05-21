# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxval = [0]
        self.helper(root, maxval)
        return maxval[0]
        
    def helper(self, node, maxval):
        if node == None:
            return (0, 0)
            
        left = self.helper(node.left, maxval)
        right = self.helper(node.right, maxval)
        decr = inr = 1
        
        if node.left != None:
            if node.left.val - node.val == 1:
                decr = left[0] + 1
            elif node.left.val - node.val == -1:
                inr = left[1] + 1
        
        if node.right != None:
            if node.right.val - node.val == 1:
                decr = max(decr, right[0] + 1)
            elif node.right.val - node.val == -1:
                inr = max(inr, right[1] + 1)
        maxval[0] = max(maxval[0], decr + inr - 1)
        
        return (decr, inr)
