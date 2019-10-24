# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        left = l = None
        right = r = None
        m = head
        node = head.next
        while node:
            if node.val == head.val:
                m.next = node
                m = node
            elif node.val < head.val:
                if not left:
                    left = node
                    l = node
                else:
                    l.next = node
                    l = l.next
            else:
                if not right:
                    right = node
                    r = node
                else:
                    r.next = node
                    r = r.next
            node.next, node = None, node.next
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        m.next = right
        if not left:
            return head
        else:
            end = left
            while end.next:
                end = end.next
            end.next = head
        
        return left
        
