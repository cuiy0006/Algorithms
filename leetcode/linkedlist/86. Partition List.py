# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        larger = ListNode()

        node1 = less
        node2 = larger
        node = head
        while node is not None:
            if node.val < x:
                node1.next = node
                node1 = node1.next
            else:
                node2.next = node
                node2 = node2.next
            node = node.next
        
        node2.next = None
        node1.next = larger.next
        return less.next