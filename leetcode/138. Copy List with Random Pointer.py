"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        node = head
        new_head = Node(0, None, None)
        new_node = new_head
        while node:
            new_node.next = Node(node.val, None, None)
            new_node = new_node.next
            dic[node] = new_node
            node = node.next
        
        node = head
        new_node = new_head.next
        while node:
            new_node.random = dic[node.random] if node.random else None
            new_node = new_node.next
            node = node.next
        return new_head.next
            
