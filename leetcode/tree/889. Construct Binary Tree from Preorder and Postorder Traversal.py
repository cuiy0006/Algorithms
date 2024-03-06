# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = { num:i for i, num in enumerate(postorder) }

        def construct(pre_i, pre_j, po_i, po_j):
            if pre_i > pre_j:
                return None
            node = TreeNode(preorder[pre_i])
            if pre_i == pre_j:
                return node

            idx = dic[preorder[pre_i+1]]
            print(preorder[pre_i+1], idx)
            node.left = construct(pre_i+1, pre_i+1+idx-po_i, po_i, idx)
            node.right = construct(pre_i+1+idx-po_i+1, pre_j, idx+1, po_j-1)
            return node

        return construct(0, len(preorder)-1, 0, len(preorder)-1)
