# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            if start is None:
                return (None, None)
            p1 = start
            p2 = start.next
            p3 = start.next
            start.next = None
            while p2 is not None:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
            return (end, start)
        
        dummy = ListNode()
        last_tail = dummy
        next_start = head

        while True:
            p = next_start
            if p is None:
                break
            n = 1
            while p.next is not None:
                p = p.next
                n += 1
                if n == k:
                    break
            if n != k:
                last_tail.next = next_start
                break
            else:
                start = next_start
                end = p
                next_start = p.next
                end.next = None
                new_start, new_end = reverse(start, end)
                last_tail.next = new_start
                last_tail = new_end

        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        cnt = 0
        while cnt < k:
            if node == None:
                return head
            cnt += 1
            node = node.next
        node = head
        tmp = None
        cnt = 0
        while cnt < k:
            node.next, node, tmp = tmp, node.next, node
            cnt += 1
        head.next = self.reverseKGroup(node, k)
        return tmp
