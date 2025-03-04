# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cnt = 0
        p = head
        tail = None
        while p is not None:
            cnt += 1
            if p.next is None:
                tail = p
            p = p.next
        
        k = k % cnt
        if k == 0:
            return head
        p1 = head
        p2 = head
        for _ in range(k):
            p1 = p1.next
        
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        new_head = p2.next
        p2.next = None
        tail.next = head
        return new_head


