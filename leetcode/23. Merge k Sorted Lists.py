# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        q = deque(lists)
        while len(q) != 1:
            first = q.popleft()
            second = q.popleft()
            head = tail = ListNode(0) 
            while first != None and second != None:
                if first.val < second.val:
                    tail.next, tail = first, first
                    first, tail.next = first.next, None
                else:
                    tail.next, tail = second, second
                    second, tail.next = second.next, None
            if first != None:
                tail.next = first
            if second != None:
                tail.next = second
            q.append(head.next)
        return q.popleft()
             

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(root1, root2):
            node = root = ListNode()
            node1 = root1
            node2 = root2
            
            while node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                    
                node = node.next
            
            while node1:
                node.next = node1
                node = node.next
                node1 = node1.next
            
            while node2:
                node.next = node2
                node = node.next
                node2 = node2.next
            return root.next
        
        q = deque(lists)
        
        while len(q) > 1:
            node1 = q.popleft()
            node2 = q.popleft()
            
            q.append(merge_two(node1, node2))
        
        return q.popleft() if len(q) > 0 else None
