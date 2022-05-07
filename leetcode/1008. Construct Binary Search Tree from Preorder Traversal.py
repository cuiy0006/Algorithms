# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            if left > right:
                return None

            node = TreeNode(preorder[left])
            i = left+1
            while i <= right:
                if preorder[i] < node.val:
                    i += 1
                else:
                    break
            
            node.left = construct(left+1, i-1)
            node.right = construct(i, right)
            return node
        
        return construct(0, len(preorder)-1)
