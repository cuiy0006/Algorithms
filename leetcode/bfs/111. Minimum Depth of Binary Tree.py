# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([root])
        height = 1
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return height
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            height += 1

