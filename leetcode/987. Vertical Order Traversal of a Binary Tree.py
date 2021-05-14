# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        col_dic = {}
        
        def traverse(node, row, col):
            if node is None:
                return
            
            if col not in col_dic:
                col_dic[col] = []
            
            col_dic[col].append((row, node.val))
            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)
            
        traverse(root, 0, 0)
        
        cols = sorted(list(col_dic.keys()))
        res = []
        for col in cols:
            row_node_lst = col_dic[col]
            row_node_lst.sort(key=lambda x:(x[0], x[1]))
            res.append([val for row, val in row_node_lst])
            
        return res
