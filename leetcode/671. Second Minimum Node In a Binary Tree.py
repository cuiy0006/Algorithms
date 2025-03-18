# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val = sys.maxsize
        second_val = sys.maxsize
        def traverse(node):
            if node is None:
                return
            nonlocal min_val
            nonlocal second_val
            min_val = min(min_val, node.val)
            if node.val > min_val and node.val < second_val:
                second_val = node.val
            if node.val < second_val:
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        return second_val if second_val != sys.maxsize else -1
