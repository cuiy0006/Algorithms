# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            if left > right:
                return None
            max_idx = left
            max_val = nums[left]
            for i in range(left+1, right+1):
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_idx = i
            
            node = TreeNode(max_val)
            node.left = build_tree(left, max_idx-1)
            node.right = build_tree(max_idx+1, right)
            return node
        
        return build_tree(0, len(nums)-1)

