# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = []
        right = []
        leaves = []
        
        if root.left != None:
            self.findLeft(root.left, left)
            self.findLeaves(root.left, leaves)
        if root.right !=None:
            self.findLeaves(root.right, leaves)
            self.findRight(root.right, right)
        right.reverse()
        return [root.val] + left + leaves + right
                    
    def findLeft(self, node, left):
        if node.left == None and node.right == None:
            return
        left.append(node.val)
        
        if node.left != None:
            self.findLeft(node.left, left)
        else:
            self.findLeft(node.right, left)
    
    def findRight(self, node, right):
        if node.left == None and node.right == None:
            return
        right.append(node.val)
        
        if node.right != None:
            self.findRight(node.right, right)
        else:
            self.findRight(node.left, right)
                
    def findLeaves(self, node, leaves):
        if node.left == None and node.right == None:
            leaves.append(node.val)
            return
        if node.left != None:
            self.findLeaves(node.left, leaves)
        if node.right != None:
            self.findLeaves(node.right, leaves)
