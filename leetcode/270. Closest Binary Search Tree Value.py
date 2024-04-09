# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = sys.maxsize
        def search(node):
            if node is None:
                return
            nonlocal res
            diff_l = abs(node.val - target)
            diff_r = abs(res - target)
            if diff_l < diff_r:
                res = node.val
            elif diff_l == diff_r:
                if node.val < res:
                    res = node.val
            if node.val >= target:
                search(node.left)
            else:
                search(node.right)
        search(root)
        return res
