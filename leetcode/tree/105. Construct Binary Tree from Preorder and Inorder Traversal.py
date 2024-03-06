# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = { num:i for i, num in enumerate(inorder) }

        def construct(pre_i, pre_j, in_i, in_j):
            if pre_i > pre_j:
                return None
            node = TreeNode(preorder[pre_i])
            idx = dic[node.val]

            node.left = construct(pre_i+1, pre_i+idx-in_i, in_i, idx-1)
            node.right = construct(pre_i+idx-in_i+1, pre_j, idx+1, in_j)
            return node

        return construct(0, len(preorder)-1, 0, len(preorder)-1)