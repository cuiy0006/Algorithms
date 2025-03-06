# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = {0:1}
        res = 0
        def traverse(node, presum):
            if node is None:
                return
            presum += node.val
            if presum-targetSum in dic:
                nonlocal res
                res += dic[presum-targetSum]
            if presum not in dic:
                dic[presum] = 0
            dic[presum] += 1
            traverse(node.left, presum)
            traverse(node.right, presum)
            dic[presum] -= 1
        
        traverse(root, 0)
        return res
