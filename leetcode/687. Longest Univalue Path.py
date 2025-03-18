# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node):
            if node is None:
                return None, 0
            left_val, left_cnt = traverse(node.left)
            right_val, right_cnt = traverse(node.right)
            cnt = 1
            lbranch = 1
            rbranch = 1
            if left_val == node.val:
                cnt += left_cnt
                lbranch += left_cnt
            if right_val == node.val:
                cnt += right_cnt
                rbranch += right_cnt
            nonlocal res
            res = max(res, cnt)

            return node.val, max(lbranch, rbranch)
        traverse(root)
        return res-1 if res > 0 else 0
            

