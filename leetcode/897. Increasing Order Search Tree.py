# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        last = None
        node = root
        lst = []
        res = None
        
        while len(lst) != 0 or node is not None:
            if node is None:
                node = lst.pop()
                if res is None:
                    res = node
                if last is not None:
                    last.right = node
                node.left = None
                last, node.right, node  = node, None, node.right
            while node is not None:
                lst.append(node)
                node = node.left
                
        return res
