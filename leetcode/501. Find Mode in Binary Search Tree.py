# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_cnt = 0
        res = []
        cnt = 0
        val = None
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nonlocal val
            nonlocal cnt
            nonlocal max_cnt
            if node.val == val:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                    res.clear()
                    res.append(val)
                elif cnt == max_cnt:
                    res.append(val)
                cnt = 0
            val = node.val
            cnt += 1
            inorder(node.right)

        inorder(root)
        if cnt > max_cnt:
            max_cnt = cnt
            res.clear()
            res.append(val)
        elif cnt == max_cnt:
            res.append(val)

        return res
