# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#better, tmp, tmp.next, node = node, tmp, node.next
#.......reserve node, tmp, node.next in memory, then assign to left hand side(LHS) from left to right
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        tmp = None
        while node != None:
            tmp, tmp.next, node = node, tmp, node.next 
        return tmp


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
