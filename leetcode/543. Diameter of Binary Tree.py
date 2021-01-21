# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0]
        
        def helper(node):
            if node == None:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            diameter[0] = max(diameter[0], left + right)
            
            return max(left, right) + 1
        
        helper(root)
        
        return diameter[0]
