# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        def traverse(node):
            if node is None:
                return
            nonlocal total
            total += node.val
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)

        curr = 0
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nonlocal curr
            nonlocal total
            node.val, curr = total - curr, curr + node.val
            inorder(node.right)
        inorder(root)

        return root