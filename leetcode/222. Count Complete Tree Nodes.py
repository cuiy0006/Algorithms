# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_cnt = 0
        node = root
        while node is not None:
            node = node.left
            left_cnt += 1
        right_cnt = 0
        node = root
        while node is not None:
            node = node.right
            right_cnt += 1
        cnt = 0
        if left_cnt == right_cnt:
            cnt += 2 ** left_cnt - 1
        else:
            cnt += self.countNodes(root.left)
            cnt += self.countNodes(root.right)
            cnt += 1
        return cnt
