# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= 1
        vhead = ListNode()
        vhead.next = head
        p1 = vhead
        
        idx = 0
        while idx < left:
            p1 = p1.next
            idx += 1
        
        left = p1.next
        p2 = left
        while idx < right:
            p2 = p2.next
            idx += 1
        right = p2
        p2 = p2.next

        x = left
        y = left.next
        x.next = None
        
        while y != p2:
            x, y.next, y = y, x, y.next
        
        p1.next = right
        left.next = p2

        return vhead.next
        
