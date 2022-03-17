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
