# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def helper(node):
            if node == None:
                return (0, None)
            next_idx, next_node = helper(node.next)
            if next_idx == n:
                node.next = node.next.next
            return (next_idx + 1, node)
        
        idx, head = helper(head)
        if idx == n:
            return head.next
        else:
            return head
