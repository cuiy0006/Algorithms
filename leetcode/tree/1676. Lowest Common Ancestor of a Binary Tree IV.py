# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        s = set([node.val for node in nodes])
        res = None
        def traverse(node):
            if node is None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            cnt = left + right
            if node.val in s:
                cnt += 1
            nonlocal res
            if cnt == len(s) and res is None:
                res = node
            return cnt
        traverse(root)
        return res 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        s = set([node.val for node in nodes])
        def helper(node):
            if node is None:
                return None, 0
            left, left_cnt = helper(node.left)
            right, right_cnt = helper(node.right)
            if node.val in s:
                return node, left_cnt + right_cnt + 1
            if left_cnt != 0 and right_cnt != 0:
                return node, left_cnt + right_cnt
            if left_cnt != 0:
                return left, left_cnt
            if right_cnt != 0:
                return right, right_cnt
            return None, 0
        
        ancestor, _ = helper(root)
        return ancestor
