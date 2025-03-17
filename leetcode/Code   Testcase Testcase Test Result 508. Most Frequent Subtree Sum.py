# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        def traverse(node):
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            sumval = left + right + node.val
            if sumval not in dic:
                dic[sumval] = 0
            dic[sumval] += 1
            return sumval
        traverse(root)
        maxfreq = max(dic.values())
        
        return [val for val, freq in dic.items() if freq == maxfreq]
