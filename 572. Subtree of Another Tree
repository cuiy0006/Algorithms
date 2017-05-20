class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, x, y):
        if x == None and y == None:
            return True
        
        if (x == None and y != None) or (x != None and y == None):
            return False
        
        if x.val != y.val:
            return False
            
        return self.isSameTree(x.left, y.left) and self.isSameTree(x.right, y.right)
