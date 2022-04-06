# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        l_to_r = False
        q = deque([root])
        res = []
        
        while len(q) != 0:
            size = len(q)
            node_lst = []
            res_lst = []
            
            while size != 0:
                node = q.popleft()
                res_lst.append(node.val)
                if l_to_r:
                    if node.right is not None:
                        node_lst.append(node.right)
                    if node.left is not None:
                        node_lst.append(node.left)
                else:
                    if node.left is not None:
                        node_lst.append(node.left)
                    if node.right is not None:
                        node_lst.append(node.right)
                size -= 1
            
            l_to_r = not l_to_r
            res.append(res_lst)
            while len(node_lst) != 0:
                q.append(node_lst.pop())
        return res
