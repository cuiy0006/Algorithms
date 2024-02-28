# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        for i in range(n):
            node = node.next
        if node is None:
            return head.next
        
        node = node.next
        parent = head
        while node is not None:
            parent = parent.next
            node = node.next
        parent.next = parent.next.next
        return head
