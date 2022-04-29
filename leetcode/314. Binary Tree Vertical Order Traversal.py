# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        dic = defaultdict(list)
        
        q = deque([(root, 0)])
        
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                node, idx = q.popleft()
                dic[idx].append(node.val)
                if node.left is not None:
                    q.append((node.left, idx-1))
                if node.right is not None:
                    q.append((node.right, idx+1))
        
        return [dic[key] for key in sorted(dic.keys())]
