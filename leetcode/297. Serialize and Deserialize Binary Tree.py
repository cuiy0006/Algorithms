# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        if root == None:
            return res
        q = deque([root])
        while len(q) != 0:
            node = q.popleft()
            if node == None:
                res += 'N#'
                continue
            res += str(node.val) + '#'
            q.append(node.left)
            q.append(node.right)
        print(res)
        return res[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        lst = data.split('#')
        root = TreeNode(lst[0])
        i = 1
        q = deque([root])
        while i < len(lst):
            node = q.popleft()
            if lst[i] == 'N':
                node.left = None
            else:
                node.left = ListNode(lst[i])
                q.append(node.left)
            if lst[i+1] == 'N':
                node.right = None
            else:
                node.right = ListNode(lst[i+1])
                q.append(node.right)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
