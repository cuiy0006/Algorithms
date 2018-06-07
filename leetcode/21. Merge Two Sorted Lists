# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        i = l1
        j = l2
        k = head
        while i and j:
            if i.val < j.val:
                k.next = i
                k = i
                i = i.next
            else:
                k.next = j
                k = j
                j = j.next
        while i:
            k.next = i
            k = i
            i = i.next
        while j:
            k.next = j
            k = j
            j = j.next            
        return head.next 
