# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        node_to_sum = {}
        
        def get_node_sum(node):
            if node is None:
                return 0
            
            left_val = get_node_sum(node.left)
            right_val = get_node_sum(node.right)
            val = node.val + left_val + right_val
            node_to_sum[node] = val
            return val
        
        get_node_sum(root)
        
        total = node_to_sum[root]
        res = 0
        def preorder(node):
            if node is None:
                return
            
            nonlocal res
            res = max(res, (total-node_to_sum[node])*node_to_sum[node])
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res % 1000000007
            
