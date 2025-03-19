# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lst = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            lst.append(node)
            inorder(node.right)
            node.left = None
            node.right = None
        
        inorder(root)

        def buildbst(i, j):
            if i > j:
                return None
            mid = (i+j)//2
            node = lst[mid]
            node.left = buildbst(i, mid-1)
            node.right = buildbst(mid+1, j)
            return node
        
        return buildbst(0, len(lst)-1)


