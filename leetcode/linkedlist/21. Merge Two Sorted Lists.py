# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        node1 = list1
        node2 = list2
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        
        node1 = node2 if node2 is not None else node1
        while node1 is not None:
            node.next = node1
            node = node.next
            node1 = node1.next
        return dummy.next