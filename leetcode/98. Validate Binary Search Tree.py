# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        node = root
        s = []
        while node != None:
            s.append(node)
            node = node.left
        
        last = None
        while len(s) != 0:
            node = s.pop()
            if last != None and last >= node.val:
                return False
            last = node.val
            node = node.right
            while node != None:
                s.append(node)
                node = node.left
        return True
