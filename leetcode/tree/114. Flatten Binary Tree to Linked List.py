# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if node is None:
                return None

            left = node.left
            right = node.right
            node.left = None
            node.right = left

            left_last = traverse(left)
            if left_last is not None:
                left_last.right = right
            else:
                node.right = right
            right_last = traverse(right)

            if right is not None:
                return right_last
            elif left is not None:
                return left_last
            else:
                return node

        traverse(root)

