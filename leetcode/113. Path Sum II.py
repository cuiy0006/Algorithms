# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def traverse(node, curr_sum, curr_lst):
            if node is None:
                return
            curr_sum += node.val
            curr_lst.append(node.val)
            if node.left is None and node.right is None:
                if curr_sum == targetSum:
                    res.append(curr_lst[:])
            traverse(node.left, curr_sum, curr_lst)
            traverse(node.right, curr_sum, curr_lst)
            curr_lst.pop()
        
        traverse(root, 0, [])
        return res
