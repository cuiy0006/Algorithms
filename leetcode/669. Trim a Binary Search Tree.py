# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root







# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def helper(node, parent, isLeft):
            if node is None:
                return
            
            helper(node.left, node, True)
            helper(node.right, node, False)
            
            if node.val < L:
                if isLeft:
                    parent.left = node.right
                else:
                    parent.right = node.right
            elif node.val > R:
                if isLeft:
                    parent.left = node.left
                else:
                    parent.right = node.left
        
        parent = TreeNode(0)
        parent.left = root
        helper(root, parent, True)
        return parent.left
    
    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def jump(node):
            while node != None:
                if node.val < low:
                    node = node.right
                elif node.val > high:
                    node = node.left
                else:
                    break
            return node
        
        def helper(node):
            if node == None:
                return
            
            if node.left != None:
                node.left = jump(node.left)
                helper(node.left)
            if node.right != None:
                node.right = jump(node.right)
                helper(node.right)
                
        root = jump(root)
        helper(root)
        return root
