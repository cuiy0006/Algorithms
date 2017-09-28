# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if node == None:
                return '#'
            return str(node.val) + '*' + helper(node.left) + helper(node.right)
        
        return helper(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(index):
            if data[index] == '#':
                return (None, index)
            word = ''
            while data[index] != '*':
                word += data[index]
                index += 1
            node = TreeNode(int(word))
            node.left, index = helper(index+1)
            node.right, index = helper(index+1)
            return (node, index)
        return helper(0)[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))










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
        if root == None:
            return ''
        res = []
        q = deque([root])
        while len(q) != 0:
            curr = q.popleft()
            res.append(str(curr.val))
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        return ','.join(res)
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        lst = data.split(',')
        root = TreeNode(int(lst[0]))
        for i in range(1, len(lst)):
            curr = int(lst[i])
            node = root
            while True:
                if curr < node.val:
                    if node.left == None:
                        node.left = TreeNode(curr)
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = TreeNode(curr)
                        break
                    else:
                        node = node.right
        return root
                        
                        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
