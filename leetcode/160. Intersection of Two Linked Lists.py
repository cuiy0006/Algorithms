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
        nodeA = headA
        nodeB = headB
        while nodeA and nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        node1 = headA
        node2 = headB
        while nodeA:
            nodeA = nodeA.next
            node1 = node1.next
        while nodeB:
            nodeB = nodeB.next
            node2 = node2.next
        
        while node1:
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next
        return None
