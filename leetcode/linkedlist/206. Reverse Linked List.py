# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        first = head
        second = head.next
        third = second
        head.next = None

        while second is not None:
            third = second.next
            second.next = first
            first = second
            second = third
        
        return first
