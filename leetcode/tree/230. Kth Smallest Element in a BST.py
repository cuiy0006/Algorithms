# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        cnt = 0

        def inorder(node):
            nonlocal cnt
            if node is None or cnt == k:
                return
            inorder(node.left)
            cnt += 1
            if cnt == k:
                nonlocal res
                res = node.val
            inorder(node.right)
        
        inorder(root)
        return res