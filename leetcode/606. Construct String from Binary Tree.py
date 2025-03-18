# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(node):
            if node is None:
                return None
            left = traverse(node.left)
            right = traverse(node.right)
            if left is None and right is None:
                return str(node.val)
            if left is None and right is not None:
                return str(node.val) + '()(' + right + ')'
            if left is not None and right is None:
                return str(node.val) + '(' + left + ')'
            return str(node.val) + '(' + left + ')(' + right + ')'

        return traverse(root) 



class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def helper(s):
            if s.left == None and s.right == None:
                return str(s.val)
            elif s.left == None and s.right != None:
                return str(s.val) + '()(' + helper(s.right) + ')' 
            elif s.left != None and s.right == None:
                return str(s.val) +  '(' + helper(s.left) + ')'
            else:
                return str(s.val) +  '(' + helper(s.left) + ')(' + helper(s.right) + ')' 
        
        if t == None:
            return ''
        return helper(t)
