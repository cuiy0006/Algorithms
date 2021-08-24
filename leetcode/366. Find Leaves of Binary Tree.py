# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        
        def postorder(node):
            if node is None:
                return 0
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            depth = max(left, right) + 1
            if depth not in dic:
                dic[depth] = []
            dic[depth].append(node.val)
            
            return depth
        
        postorder(root)
        
        i = 1
        res = []
        while i in dic:
            res.append(dic[i])
            i += 1
        return res
