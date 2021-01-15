# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        first = head
        second = head.next
        dummy = ListNode()
        dummy.next = first
        p = dummy

        while second != None:
            p.next = second
            first.next, second.next = second.next, first
            p = first
            first = first.next
            if first == None:
                break
            second = first.next
        return dummy.next
