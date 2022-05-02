# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        stack = []
        node = root
        while node != None:
            stack.append(node)
            node = node.left
        
        node = root = stack.pop()
        while len(stack) != 0:
            origin_root = stack.pop()
            node.left = origin_root.right
            node.right = origin_root
            origin_root.left = origin_root.right = None
            node = origin_root
            
        return root

    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.left is None:
            return root
        
        proot = root
        while proot.left is not None:
            proot = proot.left
            
        def helper(node):
            if node is None or node.left is None:
                return
            
            new_root = node.left
            new_left = node.right
            new_right = node
            
            helper(node.left)
            new_root.left = new_left
            new_root.right = new_right
            node.left = None
            node.right = None
            
        helper(root)
        return proot
