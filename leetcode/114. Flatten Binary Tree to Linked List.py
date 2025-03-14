# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        dummy = TreeNode()
        parent = dummy
        def preorder(node):
            if node is None:
                return
            left = node.left
            right = node.right
            node.left = None
            nonlocal parent
            parent.right = node
            parent = node
            preorder(left)
            preorder(right)
        
        preorder(root)



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
