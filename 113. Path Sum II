# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(curr_lst, node, curr_val):
            if node.left is None and node.right is None:
                if curr_val + node.val == sum:
                    curr_lst.append(node.val)
                    res.append(curr_lst[:])
                    curr_lst.pop()
                    return
            else:
                curr_lst.append(node.val)
                if node.left is not None:
                    helper(curr_lst, node.left, curr_val + node.val)
                if node.right is not None:
                    helper(curr_lst, node.right, curr_val + node.val)
                curr_lst.pop()
        if root is None:
            return []
        helper([], root, 0)
        return res
