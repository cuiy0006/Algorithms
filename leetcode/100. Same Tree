# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        stack1 = [p]
        stack2 = [q]
        while len(stack1) != 0:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack1.append(node1.right)
                stack1.append(node1.left)
                stack2.append(node2.right)
                stack2.append(node2.left)
        return True
