# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self_cnt = 0
        left_cnt = 0
        right_cnt = 0

        def traverse(node):
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            cnt = left+right+1
            if node.val == x:
                nonlocal self_cnt
                nonlocal left_cnt
                nonlocal right_cnt
                self_cnt = cnt
                left_cnt = left
                right_cnt = right
            return cnt
        
        traverse(root)
        if n - self_cnt > self_cnt:
            return True
        if left_cnt > n - left_cnt:
            return True
        if right_cnt > n - right_cnt:
            return True
        return False
