# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    
    def buildTreeHelper(self, preorder, pstart, pend, inorder, istart, iend):
        if pstart > pend:
            return None
        root = TreeNode(preorder[pstart])
        idx = inorder.index(preorder[pstart], istart, iend+1)
        left_cnt = idx - istart
        root.left = self.buildTreeHelper(preorder, pstart+1, pstart+left_cnt, inorder, istart, idx-1)
        root.right = self.buildTreeHelper(preorder, pstart+left_cnt+1, pend, inorder, idx+1, iend)
        return root
