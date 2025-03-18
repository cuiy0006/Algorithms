# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dic = {}
        def traverse_depth(node, d):
            if node is None:
                return
            if d not in dic:
                dic[d] = 0
            dic[d] += 1
            traverse_depth(node.left, d+1)
            traverse_depth(node.right, d+1)
        traverse_depth(root, 0)
        max_depth = max(dic.keys())
        cnt = dic[max_depth]
        res = None
        def traverse(node, d):
            if node is None:
                return 0
            left = traverse(node.left, d+1)
            right = traverse(node.right, d+1)
            curr = left+right
            if d == max_depth:
                curr += 1
            nonlocal res
            if curr == cnt and res is None:
                res = node
            return curr
        traverse(root, 0)
        return res


