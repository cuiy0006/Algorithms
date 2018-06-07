# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root_val = preorder[0]
        index = inorder.index(root_val)
        root = TreeNode(root_val)
        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]
        preorder_left = preorder[1:index+1]
        preorder_right = preorder[index+1:]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
