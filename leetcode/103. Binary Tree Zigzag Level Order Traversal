# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        left_first = True
        stack = [root]
        res = []
        while len(stack) != 0:
            cnt = len(stack)
            curr = []
            new_stack = []
            while cnt != 0:
                node = stack.pop()
                curr.append(node.val)
                if left_first:
                    if node.left is not None:
                        new_stack.append(node.left)
                    if node.right is not None:
                        new_stack.append(node.right)
                else:
                    if node.right is not None:
                        new_stack.append(node.right)
                    if node.left is not None:
                        new_stack.append(node.left)
                cnt -= 1
            left_first = not left_first
            stack = new_stack
            res.append(curr)
        return res
