# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def traverse(node, presum):
            if node is None:
                return None
            presum += node.val
            left = traverse(node.left, presum)
            right = traverse(node.right, presum)
            if left is not None and presum + left < limit:
                node.left = None
            if right is not None and presum + right < limit:
                node.right = None

            if left is None and right is None:
                return node.val
            if left is None:
                return right + node.val
            if right is None:
                return left + node.val
            return max(left, right) + node.val

        if traverse(root, 0) < limit:
            return None
        return root
