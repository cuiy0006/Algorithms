# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        l = 0
        node = head
        tail = None
        
        while node is not None:
            tail = node
            node = node.next
            l += 1
        
        k = (l - k % l) % l
        if k == 0:
            return head
        
        node = head
        parent = None
        while k != 0:
            parent = node
            node = node.next
            k -= 1
        
        parent.next = None
        tail.next = head
        return node
        
        
