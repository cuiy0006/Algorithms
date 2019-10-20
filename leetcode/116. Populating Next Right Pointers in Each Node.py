"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while len(q) != 0:
            size = len(q)
            while size != 0:
                size -= 1
                node = q.popleft()
                if size == 0:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
