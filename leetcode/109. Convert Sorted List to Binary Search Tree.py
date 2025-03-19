# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        p = head
        n = 0
        while p is not None:
            p = p.next
            n += 1
        
        p = head
        def inorder(i, j):
            if i > j:
                return None
            mid = (i+j)//2
            left = inorder(i, mid-1)
            nonlocal p
            node = TreeNode(p.val)
            p = p.next
            right = inorder(mid+1, j)
            node.left = left
            node.right = right
            return node
        return inorder(0, n-1)
