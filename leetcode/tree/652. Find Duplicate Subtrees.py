# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        hashes = defaultdict(int)

        def traverse(node):
            if node is None:
                return 'N'

            hash_val = str(node.val) + '#' + traverse(node.left) + '#' + traverse(node.right)
            if hashes[hash_val] == 1:
                res.append(node)
            hashes[hash_val] += 1
            return hash_val

        traverse(root)
        return res

