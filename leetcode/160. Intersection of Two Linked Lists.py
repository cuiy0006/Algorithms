# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        first = headA
        second = headB
        while first != None and second != None:
            first, second = first.next, second.next
        nodeA, nodeB = headA, headB
        while first != None:
            nodeA, first = nodeA.next, first.next
        while second != None:
            nodeB, second = nodeB.next, second.next
        while nodeA != nodeB:
            nodeA, nodeB = nodeA.next, nodeB.next
        return nodeA
