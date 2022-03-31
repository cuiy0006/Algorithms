"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        s = set()
        node = p
        while node is not None:
            s.add(node)
            node = node.parent
        
        node = q
        while node is not None:
            if node in s:
                return node
            node = node.parent
            
        return None
