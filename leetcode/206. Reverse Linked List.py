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
            


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        first = head
        second = third = head.next
        first.next = None
        while second is not None:
            third = third.next
            second.next= first
            first, second = second, third
        return first
