# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        def traverse(n):
            if n == 1:
                return [TreeNode(0)]
            res = []
            for i in range(2, n, 2):
                left = traverse(i-1)
                right = traverse(n-i)
                for l in left:
                    for r in right:
                        res.append(TreeNode(0, l, r))
            return res
        
        return traverse(n)
