class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def helper(s):
            if s.left == None and s.right == None:
                return str(s.val)
            elif s.left == None and s.right != None:
                return str(s.val) + '()(' + helper(s.right) + ')' 
            elif s.left != None and s.right == None:
                return str(s.val) +  '(' + helper(s.left) + ')'
            else:
                return str(s.val) +  '(' + helper(s.left) + ')(' + helper(s.right) + ')' 
        
        if t == None:
            return ''
        return helper(t)
