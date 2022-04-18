# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def helper(node) -> (int, int): # (moves, requested)
            if node is None:
                return (0, 0)
            
            lmoves, lrequested = helper(node.left)
            rmoves, rrequested = helper(node.right)
            
            coins = node.val
            moves = lmoves + rmoves
            
            requested = 1 - coins + lrequested + rrequested
            moves += abs(requested)
            
            return (moves, requested)
        
        moves, _ = helper(root)
        
        return moves
            
