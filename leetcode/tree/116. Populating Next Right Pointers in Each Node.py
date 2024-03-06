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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        q = deque([root])
        while len(q) != 0:
            last = None
            for i in range(len(q)):
                node = q.popleft()
                if i != 0:
                    last.next = node
                last = node
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        return root
