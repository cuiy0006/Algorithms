# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_val = [-sys.maxsize]
        def helper(node):
            if not node:
                return 0
            left_max = helper(node.left)
            right_max = helper(node.right)
            node_max = node.val
            if left_max > 0:
                node_max += left_max
            if right_max > 0:
                node_max += right_max
            max_val[0] = max(max_val[0], node_max)
            return max(left_max, right_max, 0) + node.val
        helper(root)
        return max_val[0]
