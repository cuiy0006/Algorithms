# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        def traverse(node):
            if node is None:
                return None
            
            left = traverse(node.left)
            right = traverse(node.right)
            c = chr(ord('a') + node.val)
            if left is None and right is None:
                return [c]
            lst = []
            if left is not None:
                lst += left
            if right is not None:
                lst += right
            for i in range(len(lst)):
                lst[i] += c
            return lst

        return min(traverse(root))
