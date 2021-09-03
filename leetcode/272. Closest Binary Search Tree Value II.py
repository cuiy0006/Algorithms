# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        lst = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            lst.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        left = 0
        right = len(lst) - 1
        
        while right - left >= k:
            if abs(lst[left] - target) > abs(lst[right] - target):
                left += 1
            else:
                right -= 1
        
        return lst[left:right+1]
      
      
      
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush, heappop

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        heap = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            
            heappush(heap, (-abs(node.val - target), node.val))
            if len(heap) > k:
                heappop(heap)
            
            inorder(node.right)
            
        inorder(root)
        
        return [val for diff, val in heap]
