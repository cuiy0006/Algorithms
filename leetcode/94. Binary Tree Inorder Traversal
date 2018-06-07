# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        s = []
        res = []
        while len(s) != 0 or node != None:
            if len(s) != 0:
                node = s.pop()
                res.append(node.val)
                node = node.right
            while node != None:
                s.append(node)
                node = node.left
                
        return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(node):
            if node is None:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res
