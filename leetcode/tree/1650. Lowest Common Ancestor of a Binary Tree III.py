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
        ancestors = {}
        node = p
        while node is not None:
            ancestors[node.val] = node
            node = node.parent
        
        node = q
        while node is not None:
            if node.val in ancestors:
                return ancestors[node.val]
            node = node.parent

        return None

