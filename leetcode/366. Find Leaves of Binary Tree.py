# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = {}
        
        def go_depth(node):
            if node is None:
                return 0
            
            depth = max(go_depth(node.right), go_depth(node.left)) + 1
            if depth not in dic:
                dic[depth] = []
            dic[depth].append(node.val)
        
            return depth
        
        depth = go_depth(root)
        
        return [dic[i] for i in range(1, depth+1)]
