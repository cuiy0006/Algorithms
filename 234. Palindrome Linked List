# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        tmp = None
        while fast and fast.next:
            fast = fast.next.next
            tmp, tmp.next, slow = slow, tmp, slow.next
        if fast != None:
            slow = slow.next
        while tmp:
            if tmp.val != slow.val:
                return False
            tmp = tmp.next
            slow = slow.next
        return True
