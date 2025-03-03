# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        parent = dummy
        p1 = head
        p2 = head.next
        p3 = head.next.next
        while True:
            p3 = p2.next
            parent.next = p2
            p2.next = p1
            parent = p1
            if p3 is None or p3.next is None:
                parent.next = p3
                break
            else:
                p1 = p3
                p2 = p3.next
        
        return dummy.next
        
