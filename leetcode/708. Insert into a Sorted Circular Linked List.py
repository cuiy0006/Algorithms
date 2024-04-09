"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        insert = Node(insertVal)
        if head is None:
            insert.next = insert
            return insert
        
        first = head
        second = head.next
        while True:
            if insertVal >= first.val and insertVal <= second.val:
                first.next = insert
                insert.next = second
                break
            if second.val < first.val and (insertVal >= first.val or insertVal <= second.val):
                first.next = insert
                insert.next = second
                break
            first = second
            second = second.next
            if first == head:
                first.next = insert
                insert.next = second
                break
        
        return head
