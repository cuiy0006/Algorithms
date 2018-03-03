# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        dic = {}
        q = deque([(0, root)])
        while len(q) != 0:
            depth, node = q.popleft()
            if depth in dic:
                dic[depth].append(node.val)
            else:
                dic[depth] = [node.val]
            
            if node.left != None:
                q.append((depth - 1, node.left))
            if node.right != None:
                q.append((depth + 1, node.right))

        return [dic[key] for key in sorted(list(dic.keys()))]
