# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        p1 = head
        p2 = head.next
        p1.next = None
        while p2 is not None:
            p2.next, p2, p1 = p1, p2.next, p2
        return p1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        first = head
        second = head.next
        head.next = None
        
        while second != None:
            first, second.next, second = second, first, second.next
        
        return first
            

