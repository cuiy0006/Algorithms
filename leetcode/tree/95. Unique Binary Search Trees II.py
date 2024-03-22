# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        res = []

        def build_tree(i, j):
            if i > j:
                return [None]
            res = []
            for k in range(i, j+1):
                left = build_tree(i, k-1)
                right = build_tree(k+1, j)
                for lnode in left:
                    for rnode in right:
                        node = TreeNode(k)
                        node.left = lnode
                        node.right = rnode
                        res.append(node)
            return res
        
        return build_tree(1, n)

