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
    def inorderSuccessor(self, root: 'Node') -> 'Optional[Node]':
        if root is None:
            return None
        
        curr = root
        while root.parent is not None:
            root = root.parent
        
        node = root
        stack = []
        
        found = False
        while node is not None or len(stack) != 0:
            while node is not None:
                stack.append(node)
                node = node.left
            
            if len(stack) != 0:
                node = stack.pop()
                if found:
                    return node
                if node == curr:
                    found = True
                node = node.right
        

        return None
