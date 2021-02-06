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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        
        last = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            last = slow
            slow = slow.next
            fast = fast.next.next
            
        if last is not None:
            last.next = None
            left = head
        else:
            left = None
            
        right = slow.next
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root
        
