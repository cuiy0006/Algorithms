# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def is_sym(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is not None:
                if node1.val != node2.val:
                    return False
                return is_sym(node1.left, node2.right) and is_sym(node1.right, node2.left)
            else:
                return False
        
        return is_sym(root.left, root.right)

    
    
    
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
