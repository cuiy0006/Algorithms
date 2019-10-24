# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = 0
        head = ListNode(0)
        node = head
        while l1 or l2:
            val = tmp
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            tmp = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
        if tmp != 0:
            node.next = ListNode(tmp)
        return head.next
