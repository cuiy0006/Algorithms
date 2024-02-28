# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        last = None
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow_next = slow.next
            slow.next = last
            last = slow
            slow = slow_next

        if fast is not None:
            slow = slow.next
        
        while slow is not None:
            if slow.val != last.val:
                return False
            slow = slow.next
            last = last.next
        return True