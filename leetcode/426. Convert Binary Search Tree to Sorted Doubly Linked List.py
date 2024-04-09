"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        dummy = Node(None)
        p = dummy
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nonlocal p
            p.right = node
            node.left = p
            p = node
            inorder(node.right)

        inorder(root)
        head = dummy.right
        head.left = p
        p.right = head
        return head