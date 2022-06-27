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
        x = left
        y = left.next
        x.next = None
        
        while idx < right:
            x, y.next, y = y, x, y.next
            idx += 1
        
        p1.next = x
        left.next = y

        return vhead.next
        
        
