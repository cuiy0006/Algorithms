# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        
        p1 = head
        p2 = None
        p3= head
        
        while p3 != None and p3.next != None:
            p3 = p3.next.next
            p1.next, p1, p2 = p2, p1.next, p1
            
        if p3 != None:
            p1 = p1.next
        
        while p1 != None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
