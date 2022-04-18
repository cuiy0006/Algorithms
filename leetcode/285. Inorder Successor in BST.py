# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        node = root
        lst = []
        found = False
        
        while node is not None or len(lst) != 0:
            while node is not None:
                lst.append(node)
                node = node.left

            if len(lst) != 0:
                node = lst.pop()
                
            if found:
                return node
            if node == p:
                found = True

            node = node.right

        return None
