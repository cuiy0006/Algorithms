# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash_to_cnt = defaultdict(int)
        res = []
        
        def sub_tree_hash(node):
            if node is None:
                return 'N'
            
            h = str(node.val)
            h += '#' + sub_tree_hash(node.left) + '#' + sub_tree_hash(node.right)
            hash_to_cnt[h] += 1
            if hash_to_cnt[h] == 2:
                res.append(node)
            return h
                
        sub_tree_hash(root)
        return res
