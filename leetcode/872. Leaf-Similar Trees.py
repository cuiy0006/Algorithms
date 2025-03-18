# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getseq(root):
            seq = []
            def traverse(node):
                if node is None:
                    return
                if node.left is None and node.right is None:
                    seq.append(node.val)
                traverse(node.left)
                traverse(node.right)
            traverse(root)
            return seq
        
        seq1 = getseq(root1)
        seq2 = getseq(root2)
        return seq1 == seq2

