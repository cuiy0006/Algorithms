# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        s_direction = []
        d_direction = []
        
        def helper(node):
            if node is None:
                return None
            
            left = helper(node.left)
            right = helper(node.right)
            
            if node.val == startValue:
                if left == 'd':
                    d_direction.append('L')
                    return None
                elif right == 'd':
                    d_direction.append('R')
                    return None
                else:
                    return 's'
            
            elif node.val == destValue:
                if left == 's' or right == 's':
                    s_direction.append('U')
                    return None
                else:
                    return 'd'
            
            else:
                if left == 's' and right == 'd':
                    s_direction.append('U')
                    d_direction.append('R')
                    return None
                elif left == 'd' and right == 's':
                    s_direction.append('U')
                    d_direction.append('L')
                    return None
                elif left == 's' or right == 's':
                    s_direction.append('U')
                    return 's'
                elif left == 'd':
                    d_direction.append('L')
                    return 'd'
                elif right == 'd':
                    d_direction.append('R')
                    return 'd'
                else:
                    return None
                
                
        helper(root)
        d_direction.reverse()
        direction = s_direction + d_direction
        return ''.join(direction)
