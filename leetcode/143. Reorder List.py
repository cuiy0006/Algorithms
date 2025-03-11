
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        stack = []
        node = head
        while node is not None:
            stack.append(node)
            node = node.next
        
        p1 = None
        p2 = head
        node = None
        while p2 is not None:
            if node is not None:
                node.next = p2
            p3 = p2.next
            p2.next = None
            node = stack.pop()
            if node == p1 or node == p2:
                break
            p1 = p2
            p2.next = node
            node.next = None
            p2 = p3
        return head

        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        last = None
        
        while fast is not None and fast.next is not None:
            last = slow
            slow = slow.next
            fast = fast.next.next
            
        
        if fast is not None:
            last = slow
            slow = slow.next
            
        last.next = None
        
        p1 = slow
        p2 = slow.next

        while p2 is not None:
            p2.next, p2, p1 = p1, p2.next, p2
        
        slow.next = None
        new_head = head
        node1 = head
        node2 = p1
        
        while node1 is not None and node2 is not None:
            node1.next, node2.next, node1, node2 = node2, node1.next, node1.next, node2.next
            
        
            
        
