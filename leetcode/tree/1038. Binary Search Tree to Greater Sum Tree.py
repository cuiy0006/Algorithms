# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node, presum):
            if node is None:
                return presum
            
            presum = traverse(node.right, presum)
            node.val += presum
            return traverse(node.left, node.val)

        traverse(root, 0)
        return root
