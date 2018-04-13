# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        s = [root]
        while len(s) != 0:
            node = s.pop()
            res.append(node.val)
            if node.right != None:
                s.append(node.right)
            if node.left != None:
                s.append(node.left)
        return res  


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(node):
            if node is None:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return res
