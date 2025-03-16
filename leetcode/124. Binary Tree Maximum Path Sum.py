# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def traverse(node, presum):
            if node is None:
                return -sys.maxsize
            
            presum += node.val
            left = traverse(node.left, presum)
            right = traverse(node.right, presum)

            max_sum = node.val
            if left > presum:
                max_sum += left-presum
            if right > presum:
                max_sum += right-presum
            nonlocal res
            res = max(res, max_sum)

            return max(presum, left, right)
        
        traverse(root, 0)
        return res

