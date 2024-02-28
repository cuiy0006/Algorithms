# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left != 1:
            i = 1
            node = head
            while i < left-1:
                i += 1
                node = node.next
            parent = node
            start = parent.next
        else:
            parent = None
            start = head

        first = start
        second = start.next
        third = second
        i = left
        while i < right:
            third = second.next
            second.next = first
            first = second
            second = third
            i += 1
        start.next = second
        if parent is not None:
            parent.next = first
            return head
        else:
            return first