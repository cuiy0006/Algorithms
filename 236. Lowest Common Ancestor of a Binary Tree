# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None:
            return root
        if left == None:
            return right
        if right == None:
            return left
        return None


#my own
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        dic = {root:None}
        def helper(node):
            if node.left != None:
                dic[node.left] = node
                helper(node.left)
            if node.right != None:
                dic[node.right] = node
                helper(node.right)
        
        helper(root)
        p_ancestors = set()
        node = p
        while node != None:
            p_ancestors.add(node)
            node = dic[node]
        node = q
        while node != None:
            if node in p_ancestors:
                return node
            node = dic[node]
        return None
