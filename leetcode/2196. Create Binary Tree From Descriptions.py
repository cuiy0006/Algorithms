# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        parents = set()
        children = set()
        
        val_to_node = {}
        
        for [p, c, isleft] in descriptions:
            if p not in val_to_node:
                val_to_node[p] = TreeNode(p)
            if c not in val_to_node:
                val_to_node[c] = TreeNode(c)
            if isleft:
                val_to_node[p].left = val_to_node[c]
            else:
                val_to_node[p].right = val_to_node[c]
            
            if val_to_node[p] not in parents:
                parents.add(val_to_node[p])
            if val_to_node[c] not in children:
                children.add(val_to_node[c])
                
        root = parents - children
        
        return list(root)[0]
