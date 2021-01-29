# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        lst = [s]
        while len(lst) != 0:
            node = lst.pop()
            if self.isSame(node, t):
                return True
            if node.right != None:
                lst.append(node.right)
            if node.left != None:
                lst.append(node.left)
        return False
    
    def isSame(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        return node1.val == node2.val and self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)
