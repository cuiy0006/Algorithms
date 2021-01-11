# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        if fast == None or fast.next == None:
            return None

        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next

        return slow
