# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(top, bottom, node):
            if node is None:
                return True
            if (node.left is None or node.val > node.left.val and node.left.val > bottom) and \
            (node.right is None or node.val < node.right.val and node.right.val < top):
                return helper(node.val, bottom, node.left) and helper(top, node.val, node.right)
            return False
        return helper(sys.maxsize, -sys.maxsize, root)
                

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        last = [-sys.maxsize]
        def helper(node):
            if node == None:
                return True
            left = helper(node.left)
            mid = node.val > last[0]
            last[0] = node.val
            right = helper(node.right)
            return left and mid and right
        return helper(root)
