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
        def traverse(node):
            if node is None:
                return 'N'
            return str(node.val) + '#' + traverse(node.left) + '#' + traverse(node.right)
        return traverse(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split('#')
        def traverse(i):
            if vals[i] == 'N':
                return None, i+1
            node = TreeNode(int(vals[i]))
            i += 1
            node.left, i = traverse(i)
            node.right, i = traverse(i)
            return node, i
        
        root, _ = traverse(0)
        return root