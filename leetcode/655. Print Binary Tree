from collections import deque
class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def helper(left, right, y, lst, node):
            if node == None:
                return
            mid = (left + right) // 2
            lst[y][mid] = str(node.val)
            helper(left, mid-1, y+1, lst, node.left)
            helper(mid+1, right, y+1, lst, node.right)
            
        
        height = 0
        q = deque([root])
        while len(q) != 0:
            cnt = len(q)
            if cnt != 0:
                height += 1
            while cnt != 0:
                cnt -= 1
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        width = 0
        for i in range(height):
            width += 2**i
        lst = [["" for j in range(width)] for i in range(height)]
        helper(0, width -1, 0, lst, root)
        return lst
