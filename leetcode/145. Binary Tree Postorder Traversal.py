# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        finished = root
        s = [root]
        while len(s) != 0:
            node = s[-1]
            if node.left == None and node.right == None or node.left == finished or node.right == finished:
                res.append(node.val)
                finished = node
                s.pop()
            else:
                if node.right != None:
                    s.append(node.right)
                if node.left != None:
                    s.append(node.left)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        res = []
        lst = [root]
        
        while len(lst) != 0:
            node = lst.pop()
            res.append(node.val)
            if node.left != None:
                lst.append(node.left)
            if node.right != None:
                lst.append(node.right)
            
        return reversed(res)
