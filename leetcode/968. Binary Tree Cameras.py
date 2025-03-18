# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if node is None:
                return 0, False, False
            if node.left is None and node.right is None:
                return 0, False, True

            lcnt, l_is_camera, l_need_camera = traverse(node.left)
            rcnt, r_is_camera, r_need_camera = traverse(node.right)
            cnt = lcnt + rcnt
            is_camera = False
            need_camera = True
            if l_need_camera or r_need_camera:
                cnt += 1
                is_camera = True
                need_camera = False
            else:
                if l_is_camera or r_is_camera:
                    need_camera = False
            return cnt, is_camera, need_camera
        
        cnt, is_camera, need_camera = traverse(root)
        if not is_camera and need_camera:
            cnt += 1
        return cnt


