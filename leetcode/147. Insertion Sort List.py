# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        node = head
        while node is not None:
            next_node = node.next
            node.next = None

            p = dummy
            while p.next is not None and p.next.val < node.val:
                p = p.next
            if p.next is None:
                p.next = node
            else:
                p.next, node.next = node, p.next

            node = next_node
            
            # print(dummy.next)
        
        return dummy.next
