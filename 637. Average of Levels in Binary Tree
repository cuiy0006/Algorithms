from collections import deque
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if root == None:
            return res
        q = deque([root])
        while len(q) != 0:
            cnt = len(q)
            total = 0
            for i in range(cnt):
                node = q.popleft()
                total += node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            res.append(total / cnt)
        return res
            
