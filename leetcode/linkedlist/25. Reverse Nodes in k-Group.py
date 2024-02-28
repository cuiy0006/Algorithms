# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        parent = dummy
        node = head
        while True:
            i = 0
            start = node
            while i < k:
                if node is None:
                    break
                node = node.next
                i += 1

            if i < k:
                break
            
            first = start
            second = start.next
            third = second
            i = 0
            while i < k-1:
                third = second.next
                second.next = first
                first = second
                second = third
                i += 1
            
            node = second
            parent.next = first
            parent = start
            parent.next = second

        return dummy.next
            