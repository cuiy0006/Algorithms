# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        s = []
        node = root
        while node != None:
            s.append(node)
            node = node.left
            
        while len(s) != 0:
            node = s.pop()
            if node.val > p.val:
                return node
            node = node.right
            while node != None:
                s.append(node)
                node = node.left
        return None
