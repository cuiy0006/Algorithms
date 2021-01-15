# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        p1 = head
        p2 = head
        while p2 != None:
            if p2.val == p1.val:
                p2 = p2.next
            else:
                p1.next = p2
                p1 = p2
                p2 = p1.next
        p1.next = p2
        return head
