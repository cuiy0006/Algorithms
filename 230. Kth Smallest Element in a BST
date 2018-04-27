# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt = 0
        node =root
        stack = []
        
        while node is not None or len(stack) != 0:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) != 0:
                node = stack.pop()
                cnt += 1
                if cnt == k:
                    return node.val
                node = node.right
