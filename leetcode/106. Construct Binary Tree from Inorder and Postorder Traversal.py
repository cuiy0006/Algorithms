# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(inorder, postorder, il, ir, pl, pr):
            if il > ir:
                return None
            
            node = TreeNode(postorder[pr])
            i = inorder.index(postorder[pr])
            
            node.left = helper(inorder, postorder, il, i-1, pl, pl+i-il-1)
            node.right = helper(inorder, postorder, i+1, ir, pl+i-il, pr-1)
            return node
        return helper(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
