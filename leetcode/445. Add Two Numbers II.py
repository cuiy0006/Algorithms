# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if head is None:
                return None
            p1 = head
            p2 = head.next
            p3 = head.next
            head.next = None
            while p2 is not None:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
            return p1

        p1 = reverse(l1)
        p2 = reverse(l2)
        head = ListNode()
        p = head
        d = 0
        while p1 is not None or p2 is not None:
            val = d
            if p1 is not None:
                val += p1.val
                p1 = p1.next
            if p2 is not None:
                val += p2.val
                p2 = p2.next
            d = val // 10
            p.next = ListNode(val % 10)
            p = p.next
        
        if d == 1:
            p.next = ListNode(1)
        
        return reverse(head.next)

