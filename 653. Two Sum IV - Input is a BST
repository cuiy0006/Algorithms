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
