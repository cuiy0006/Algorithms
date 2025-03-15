# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])
        x_p = None
        y_p = None

        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                node, parent = q.popleft()
                if node.val == x:
                    x_p = parent
                    if parent is None:
                        return False
                elif node.val == y:
                    y_p = parent
                    if parent is None:
                        return False
                if node.left is not None:
                    q.append((node.left, node))
                if node.right is not None:
                    q.append((node.right, node))
            if x_p is not None and y_p is None or y_p is not None and x_p is None:
                return False
            if x_p is not None and y_p is not None:
                return x_p != y_p
        return False

        
