# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if node is None:
                return 0
            
            return max(get_height(node.left), get_height(node.right)) + 1
        
        height = get_height(root)
        
        width = 2 ** height - 1
        res = [["" for _ in range(width)] for _ in range(height)]
        
        def assign_node(node, left, right, depth):
            if node is None:
                return
            
            mid = (left + right) // 2
            res[depth][mid] = str(node.val)
            assign_node(node.left, left, mid-1, depth+1)
            assign_node(node.right, mid+1, right, depth+1)
            
        assign_node(root, 0, width-1, 0)
        
        return res
        








from collections import deque
class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def helper(left, right, y, lst, node):
            if node == None:
                return
            mid = (left + right) // 2
            lst[y][mid] = str(node.val)
            helper(left, mid-1, y+1, lst, node.left)
            helper(mid+1, right, y+1, lst, node.right)
            
        
        height = 0
        q = deque([root])
        while len(q) != 0:
            cnt = len(q)
            if cnt != 0:
                height += 1
            while cnt != 0:
                cnt -= 1
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        width = 0
        for i in range(height):
            width += 2**i
        lst = [["" for j in range(width)] for i in range(height)]
        helper(0, width -1, 0, lst, root)
        return lst

    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            if node is None:
                return 0
            
            return max(get_height(node.left), get_height(node.right)) + 1
        
        height = get_height(root)
        
        width = 2 ** height - 1
        res = [["" for _ in range(width)] for _ in range(height)]
        
        q = deque([(root, 0, (width - 1) // 2)])
        while len(q) != 0:
            size = len(q)
            while size != 0:
                node, x, y = q.popleft()
                res[x][y] = str(node.val)
                if node.left is not None:
                    q.append((node.left, x+1, y-2**(height-x-2)))
                if node.right is not None:
                    q.append((node.right, x+1, y+2**(height-x-2)))
                size -= 1
        
        return res
        
