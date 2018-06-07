# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {}
        curr = new_head = RandomListNode(0)
        node = head
        while node is not None:
            curr.next = RandomListNode(node.label)
            curr = curr.next
            dic[node] = curr
            node = node.next
        
        node = head
        curr = new_head.next
        while node is not None:
            if node.random is not None:
                curr.random = dic[node.random]
            curr = curr.next
            node = node.next
            
        return new_head.next
