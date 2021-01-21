# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def noSkip(node, sum):
            if node == None:
                return 0
            
            cnt = 0
            if sum == node.val:
                cnt = 1
            
            return noSkip(node.left, sum - node.val) + noSkip(node.right, sum - node.val) + cnt
        
        def skip(node, sum):
            if node == None:
                return 0
            
            return skip(node.left, sum) + skip(node.right, sum) + noSkip(node.left, sum) + noSkip(node.right, sum)
        
        
        return skip(root, sum) + noSkip(root, sum)
