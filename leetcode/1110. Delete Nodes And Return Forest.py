# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        
        def helper(node, parent, is_left):
            if node == None:
                return
            
            if node.val in to_delete:
                if node.left != None and node.left.val not in to_delete:
                    res.append(node.left)
                if node.right != None and node.right.val not in to_delete:
                    res.append(node.right)
                if parent != None:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
                
            helper(node.left, node, True)
            helper(node.right, node, False)
            
        if root != None and root.val not in to_delete:
            res.append(root)
            
        helper(root, None, None)
        return res
