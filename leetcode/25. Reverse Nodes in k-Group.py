# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        cnt = 0
        while cnt < k:
            if node == None:
                return head
            cnt += 1
            node = node.next
        node = head
        tmp = None
        cnt = 0
        while cnt < k:
            node.next, node, tmp = tmp, node.next, node
            cnt += 1
        head.next = self.reverseKGroup(node, k)
        return tmp
