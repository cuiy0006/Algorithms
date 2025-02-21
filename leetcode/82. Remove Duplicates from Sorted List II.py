# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        p = head
        while p is not None:
            curr = p
            while p.next is not None and p.val == p.next.val:
                p = p.next
            if curr != p:
                tail.next = p.next
            else:
                tail = p
            p = p.next
        return dummy.next
