"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        orig_to_copy = {}
        dummy = Node(0)
        p2 = dummy
        p1 = head
        while p1 is not None:
            p2.next = Node(p1.val)
            p2 = p2.next
            orig_to_copy[p1] = p2
            p1 = p1.next

        p1 = head
        p2 = dummy.next
        while p1 is not None:
            if p1.random is not None:
                p2.random = orig_to_copy[p1.random]
            p1 = p1.next
            p2 = p2.next
        return dummy.next

