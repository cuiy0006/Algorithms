# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        finished = root
        s = [root]
        while len(s) != 0:
            node = s[-1]
            if node.left == None and node.right == None or node.left == finished or node.right == finished:
                res.append(node.val)
                finished = node
                s.pop()
            else:
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(node):
            if node is None:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        
        helper(root)
        return res
