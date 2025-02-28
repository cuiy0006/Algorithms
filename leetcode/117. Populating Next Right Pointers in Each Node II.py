"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        q = deque([root])
        while len(q) != 0:
            size = len(q)
            curr = None
            for _ in range(size):
                if curr is None:
                    curr = q.popleft()
                else:
                    curr.next = q.popleft()
                    curr = curr.next
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
        
        return root
