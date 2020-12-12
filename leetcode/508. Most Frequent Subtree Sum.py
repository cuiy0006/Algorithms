# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return  []
        dic = {}
        def helper(node):
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            sum_val = left + right + node.val
            if sum_val not in dic:
                dic[sum_val] = 1
            else:
                dic[sum_val] += 1
            return sum_val
        helper(root)
        max_freq = max(list(dic.values()))
        res = [k for k,v in dic.items() if v == max_freq]
        return res
