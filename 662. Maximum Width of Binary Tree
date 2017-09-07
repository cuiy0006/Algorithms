# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        maxWidth = 1
        q = deque([(0, root)])
        
        while len(q) != 0:
            cnt = len(q)
            start = q[0]
            end = q[-1]
            width = end[0] - start[0] + 1
            maxWidth = max(maxWidth, width)
            
            while cnt > 0:
                cnt -= 1
                idx, node = q.popleft()
                if node.left != None:
                    q.append((idx * 2, node.left))
                if node.right != None:
                    q.append((idx * 2 + 1, node.right))
            
        return maxWidth
