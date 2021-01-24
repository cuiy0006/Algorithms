# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if left == None and right == None:
                return True
            elif right == None or left == None:
                return False
            
            if left.val != right.val:
                return False
            
            return helper(left.left, right.right) and helper(left.right, right.left)
        
        if root == None:
            return True
        return helper(root.left, root.right)

    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        left = [root.left]
        right = [root.right]
        
        while len(left) != 0:
            lnode = left.pop()
            rnode = right.pop()
            
            if lnode == None and rnode == None:
                continue
            elif lnode == None or rnode == None:
                return False
            
            if lnode.val != rnode.val:
                return False

            left.append(lnode.left)
            right.append(rnode.right)
            left.append(lnode.right)
            right.append(rnode.left)
        
        return True
