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
