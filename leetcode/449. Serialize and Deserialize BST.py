# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        lst = []
        def preorder(node):
            if node is None:
                lst.append('N')
                return
            lst.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ','.join(lst)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        lst = data.split(',')
        def preorder(i):
            if lst[i] == 'N':
                return None, i+1
            node = TreeNode(int(lst[i]))
            i += 1
            node.left, i = preorder(i)
            node.right, i = preorder(i)
            return node, i
        return preorder(0)[0]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
