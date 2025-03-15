# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = -sys.maxsize

        def traverse(node): # is_valid, sum, smallest node, largest node
            if node is None:
                return True, 0, None, None
            
            l = traverse(node.left)
            r = traverse(node.right)
            if not l[0] or not r[0]:
                return False, 0, None, None
            
            if l[3] is not None and node.val <= l[3].val:
                return False, 0, None, None
            
            if r[2] is not None and node.val >= r[2].val:
                return False, 0, None, None
            
            curr_sum = l[1] + node.val + r[1]
            nonlocal res
            res = max(res, curr_sum)
            
            smallest = l[2] if l[2] is not None else node
            largest = r[3] if r[3] is not None else node

            return True, curr_sum, smallest, largest
        
        traverse(root)
        return res if res > 0 else 0


