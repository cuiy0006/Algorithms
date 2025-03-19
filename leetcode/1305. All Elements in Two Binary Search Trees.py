# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def getlst(node):
            lst = []
            def inorder(node):
                if node is None:
                    return
                inorder(node.left)
                lst.append(node.val)
                inorder(node.right)
            inorder(node)
            return lst
        
        lst1 = getlst(root1)
        lst2 = getlst(root2)

        res = []
        i = 0
        j = 0
        while i < len(lst1) or j < len(lst2):
            if i == len(lst1):
                res.append(lst2[j])
                j += 1
            elif j == len(lst2):
                res.append(lst1[i])
                i += 1
            else:
                if lst1[i] < lst2[j]:
                    res.append(lst1[i])
                    i += 1
                else:
                    res.append(lst2[j])
                    j += 1
        return res

