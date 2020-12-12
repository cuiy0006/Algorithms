# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        i, j, k = head, head.next, head.next.next
        head = ListNode(0)
        last = head
        while True:
            i.next, j.next = None, i
            last.next = j
            last = i
            if k is None:
                break
            if k.next is None:
                last.next = k
                break
            i, j, k = k, k.next, k.next.next
        return head.next
