# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        pivot = head.val
        left = l = ListNode(0)
        right = r = ListNode(0)
        mid = m = head
        node = head.next
        
        while node is not None:
            if node.val == pivot:
                m.next, m = node, node
            elif node.val < pivot:
                l.next, l = node, node
            else:
                r.next, r = node, node
            node.next, node = None, node.next
        left = self.sortList(left.next)
        right = self.sortList(right.next)
        m.next = right
        l = left
        while l is not None:
            if l.next is None:
                break
            l = l.next
        if left is None:
            return mid
        else:
            l.next = mid
            return left
        
            
