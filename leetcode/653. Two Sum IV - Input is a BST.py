# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        node = root
        lst = []
        while node is not None or len(lst) != 0:
            if node is None:
                node = lst.pop()
                if (k - node.val) in s:
                    return True
                s.add(node.val)
                node = node.right
            while node is not None:
                lst.append(node)
                node = node.left
        return False



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        wanted = set()
        
        def iterate(node):
            if node is None:
                return False
            
            if node.val in wanted:
                return True
            
            wanted.add(k - node.val)
            if iterate(node.left) or iterate(node.right):
                return True
            return False
        
        return iterate(root)
            
