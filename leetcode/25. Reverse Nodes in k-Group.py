# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            if head is None or head.next is None:
                return head
            
            p1 = head
            p2 = head.next
            p1.next = None
            while p2 is not None:
                p2.next, p2, p1 = p1, p2.next, p2
            return p1
            
        
        root = ListNode()
        last_tail = root
        start = head
        
        while start is not None:
            end = start
            cnt = 0
            p = start
            while True:
                cnt += 1
                if cnt == k or p.next is None:
                    end = p
                    break
                p = p.next

            next_start = end.next
            end.next = None
            
            if cnt == k:
                new_head = reverse(start)
            else:
                new_head = start
            
            last_tail.next = new_head
            
            last_tail = start
            start = next_start
            
        return root.next



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
