# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        first = None
        second = None
        prev = None
        node = root
        lst = []
        while len(lst) != 0 or node != None:
            if node == None:
                node = lst.pop()
                if prev != None:
                    if first == None:
                        if node.val < prev.val:
                            first = prev
                            second = node
                    else:
                        if node.val < prev.val:
                            second = node
                prev = node
                node = node.right
                
            while node != None:
                lst.append(node)
                node = node.left
        
        first.val, second.val = second.val, first.val
