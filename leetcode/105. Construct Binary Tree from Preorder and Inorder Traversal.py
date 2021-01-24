# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder, inorder, pl, pr, il, ir):
            if pl > pr:
                return None
            node = TreeNode(preorder[pl])
            i = inorder.index(preorder[pl])
            
            node.left = helper(preorder, inorder, pl+1, pl+i-il, il, i-1)
            node.right = helper(preorder, inorder, pl+i-il+1, pr, i+1, ir)
            
            return node
        
        return helper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        node = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        
        node.left = self.buildTree(preorder[1:i+1], inorder[:i])
        node.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return node
