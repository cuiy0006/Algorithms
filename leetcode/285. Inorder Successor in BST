# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node = root
        passed = False
        stack = []
        while node != None or len(stack) != 0:
            while node != None:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack.pop()
                if passed:
                    return node
                if node == p:
                    passed = True
                node = node.right
        return None
