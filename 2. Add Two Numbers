# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = 0
        node = head = ListNode(0)
        while l1 is not None or l2 is not None:
            val = tmp
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            tmp = val // 10
            val = val % 10
            node.next = ListNode(val)
            node = node.next
            
        if tmp == 1:
            node.next = ListNode(1)
            
        return head.next






# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = head = ListNode(0)
        step = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + step
            node.next = ListNode(val % 10)
            node = node.next
            step = val //10
            l1, l2 = l1.next, l2.next
        for l in [l1, l2]:
            while l is not None:
                val = l.val + step
                node.next = ListNode(val % 10)
                node = node.next
                step = val //10
                l = l.next
        if step == 1:
            node.next = ListNode(1)
        return head.next



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = 0
        head = ListNode(0)
        node = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
            if l2 is None:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next
            
            val = val1 + val2 + tmp
            node.next = ListNode(val%10)
            tmp = val // 10
            node = node.next
        if tmp == 1:
            node.next = ListNode(1)
        return head.next
