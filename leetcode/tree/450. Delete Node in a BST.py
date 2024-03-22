# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_smallest(node):
            while node.left is not None:
                node = node.left
            return node
        
        def delete(node, key):
            if node is None:
                return None
            if node.val == key:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                smallest = find_smallest(node.right)
                node.right = delete(node.right, smallest.val)
                smallest.left = node.left
                smallest.right = node.right
                return smallest
            elif node.val > key:
                node.left = delete(node.left, key)
                return node
            else:
                node.right = delete(node.right, key)
                return node
        
        return delete(root, key)
 