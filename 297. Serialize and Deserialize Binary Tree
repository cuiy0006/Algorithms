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
        res = []
        if root == None:
            return ''
        q = deque([root])
        while len(q) != 0:
            node = q.popleft()
            if node == None:
                res.append('null')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ','.join(res)
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        res = data.split(',')
        val_q = deque(res)
        root = TreeNode(int(val_q.popleft()))
        q = deque([root])
        while len(q) != 0:
            node = q.popleft()
            left = val_q.popleft()
            right = val_q.popleft()
            if left == 'null':
                node.left = None
            else:
                node.left = TreeNode(int(left))
                q.append(node.left)
            if right == 'null':
                node.righe = None
            else:
                node.right = TreeNode(int(right))
                q.append(node.right)
        return root
        
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
