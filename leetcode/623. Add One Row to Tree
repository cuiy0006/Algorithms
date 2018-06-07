# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        level = 0
        q = deque([root])
        while len(q) != 0:
            cnt = len(q)
            level += 1
            while cnt != 0:
                cnt -= 1
                node = q.popleft()
                if level != d - 1:
                    if node.left != None:
                        q.append(node.left)
                    if node.right != None:
                        q.append(node.right)
                else:
                    left = TreeNode(v)
                    right = TreeNode(v)
                    left.left = node.left
                    right.right = node.right
                    node.left = left
                    node.right = right
            if level == d - 1:
                break
        return root
