# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        node = TreeNode(pre[0])
        if len(pre) == 1:
            return node
        
        left_root_val = pre[1]
        idx = post.index(left_root_val)
        node.left = self.constructFromPrePost(pre[1:idx+2], post[0:idx+1])
        node.right = self.constructFromPrePost(pre[idx+2:], post[idx+1:-1])
        return node
        
