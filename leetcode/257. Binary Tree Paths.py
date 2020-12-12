# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        res = []
        def helper(node, lst):
            lst.append(str(node.val))
            if node.left == None and node.right == None:
                res.append(lst)
                return
            if node.left != None:
                helper(node.left, lst[:])
            if node.right != None:
                helper(node.right, lst[:])
        helper(root, [])
        return ['->'.join(lst) for lst in res]
