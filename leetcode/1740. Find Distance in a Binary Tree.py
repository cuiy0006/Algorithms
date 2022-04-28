# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        
        def find_d(node):
            if node is None:
                return (None, 0)
            
            curr = None
            if node.val == p or node.val == q:
                curr = 'partial'
            
            left = find_d(node.left)
            right = find_d(node.right)
            
            if curr is not None:
                if left[0] is not None:
                    return ('found', left[1])
                if right[0] is not None:
                    return ('found', right[1])
                else:
                    return (curr, 1)
            else:
                if left[0] is not None and right[0] is not None:
                    return ('found', left[1]+right[1])
                elif left[0] is not None:
                    if left[0] == 'partial':
                        return ('partial', left[1]+1)
                    else:
                        return left
                elif right[0] is not None:
                    if right[0] == 'partial':
                        return ('partial', right[1]+1)
                    else:
                        return right
                else:
                    return (None, 0)
                
        return find_d(root)[1]
