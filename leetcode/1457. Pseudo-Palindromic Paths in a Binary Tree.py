# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, cnts):
            if node is None:
                return
            cnts[node.val] += 1
            if node.left is None and node.right is None:
                single = 0
                for i in range(1, 10):
                    if cnts[i] % 2 == 1:
                        single += 1
                        if single > 1:
                            break
                if single < 2:
                    nonlocal res
                    res += 1
            traverse(node.left, cnts)
            traverse(node.right, cnts)
            cnts[node.val] -= 1
        
        traverse(root, [0]*10)
        return res
