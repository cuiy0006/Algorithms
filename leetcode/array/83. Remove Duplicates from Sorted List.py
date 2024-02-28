# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        parent = head
        node = head.next
        while node is not None:
            if node.val == parent.val:
                parent.next = node.next
                node = node.next
            else:
                parent = parent.next
                node = node.next
        return head
            