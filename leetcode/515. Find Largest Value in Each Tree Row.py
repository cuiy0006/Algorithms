# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        q = deque([root])
        
        while len(q) != 0:
            size = len(q)
            max_val = -sys.maxsize
            for _ in range(size):
                node = q.popleft()
                
                max_val = max(max_val, node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
            res.append(max_val)
        
        return res
