


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







class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder(lst, node):
            if node == None:
                return
            inorder(lst, node.left)
            lst.append(node.val)
            inorder(lst, node.right)
        lst = []
        inorder(lst, root)
        left = 0
        right = len(lst) - 1
        while left < right:
            if lst[left] + lst[right] == k:
                return True
            elif lst[left] + lst[right] < k:
                left += 1
            else:
                right -=1
        return False
