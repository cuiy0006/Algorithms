# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == '':
            return None
        
        idx = 0
        while idx < len(s):
            if s[idx] == '(':
                break
            idx += 1

        val = int(s[:idx])
        cnt = 0
        i = idx
        while i < len(s):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
            if cnt == 0:
                break
            i += 1
            
        left = s[idx+1:i]
        right = s[i+2:-1]
        node = TreeNode(val)
        node.left = self.str2tree(left)
        node.right = self.str2tree(right)
        return node
