# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        min_val = root.val
        second_min = None
        
        def helper(node):
            if node is None:
                return
            
            if node.val > min_val:
                nonlocal second_min
                if second_min is None:
                    second_min = node.val
                else:
                    second_min = min(second_min, node.val)
            
            else:
                helper(node.left)
                helper(node.right)
        
        helper(root)
                
        return -1 if second_min is None else second_min
