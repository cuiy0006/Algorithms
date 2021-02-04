# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque([root])
        res = None
        while len(q) != 0:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == 0:
                    res = node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        return res
                
