# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        while node1 is not None and node2 is not None:
            node1 = node1.next
            node2 = node2.next
        
        if node1 is None:
            node = node2
            long = headB
            short = headA
        else:
            node = node1
            long = headA
            short = headB
        
        while node is not None:
            long = long.next
            node = node.next
        
        while long is not None and short is not None:
            if short == long:
                return short
            short = short.next
            long = long.next
        return None
        