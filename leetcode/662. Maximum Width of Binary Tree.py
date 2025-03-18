# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(0, root)])
        while len(q) != 0:
            size = len(q)
            start = None
            end = None
            for i in range(size):
                idx, node = q.popleft()
                if i == 0:
                    start = idx
                if i == size-1:
                    end = idx
                if node.left is not None:
                    q.append((idx*2, node.left))
                if node.right is not None:
                    q.append((idx*2+1, node.right))
            res = max(res, end-start+1)
        return res

