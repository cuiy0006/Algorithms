# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        q = deque([root])
        while len(q) != 0:
            cnt = len(q)
            while cnt != 0:
                node = q.popleft()
                cnt -= 1
                if cnt == 0:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
