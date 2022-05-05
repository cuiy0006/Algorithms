"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        q = deque([root])
        while len(q) != 0:
            size = len(q)
            p = Node()
            for _ in range(size):
                node = q.popleft()
                p.next = node
                p = node
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        
        return root
