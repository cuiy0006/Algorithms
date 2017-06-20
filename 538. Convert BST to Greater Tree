# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        lst = []
        self.inorder(root, lst)
        for i in list(range(len(lst) - 1))[::-1]:
            lst[i] += lst[i + 1]
        node = TreeNode(0)
        self.helper(root, node, deque(lst))
        return node
        
        
    def inorder(self, node, lst):
        if node == None:
            return
        self.inorder(node.left, lst)
        lst.append(node.val)
        self.inorder(node.right, lst)
        
    def helper(self, root, node, lst):
        if root.left != None:
            node.left = TreeNode(0)
            self.helper(root.left, node.left, lst)
        node.val = lst[0]
        lst.popleft()
        if root.right != None:
            node.right = TreeNode(0)
            self.helper(root.right, node.right, lst)
