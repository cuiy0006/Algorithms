# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        from_left = True
        while len(stack) != 0:
            level = []
            tmp = []
            while len(stack) != 0:
                node = stack.pop()
                level.append(node.val)
                if from_left:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                else:
                    if node.right:
                        tmp.append(node.right)
                    if node.left:
                        tmp.append(node.left)
            stack = tmp
            from_left = not from_left
            res.append(level)
        return res
        
        
