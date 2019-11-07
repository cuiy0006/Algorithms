# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        if fast != None:
            slow = slow.next
        
        last = None
        curr = slow
        while curr != None:
            curr.next, curr, last = last, curr.next, curr
        
        node1 = last
        node2 = head
        while node1 != None:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True
        
        
        
