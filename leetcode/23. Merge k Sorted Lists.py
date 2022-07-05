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

from heapq import heappush, heappop

class Node:
    def __init__(self, listnode):
        self.listnode = listnode
    
    def __lt__(self, other):
        return self.listnode.val < other.listnode.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        root = ListNode()
        curr = root
        
        for lst in lists:
            if lst is not None:
                heappush(h, Node(lst))
        
        while len(h) != 0:
            node = heappop(h)
            listnode = node.listnode
            curr.next = listnode
            curr = curr.next
            if listnode.next is not None:
                heappush(h, Node(listnode.next))
        
        return root.next
