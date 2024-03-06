# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dic = { num:i for i, num in enumerate(inorder) }

        def construct(in_i, in_j, po_i, po_j):
            if po_i > po_j:
                return None
            node = TreeNode(postorder[po_j])

            idx = dic[node.val]
            node.left = construct(in_i, idx-1, po_i, po_i+idx-in_i-1)
            node.right = construct(idx+1, in_j, po_i+idx-in_i, po_j-1)
            return node

        return construct(0, len(inorder)-1, 0, len(inorder)-1)
