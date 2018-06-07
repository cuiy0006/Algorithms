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
        lst1 = []
        lst2 = []
        while l1 is not None:
            lst1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            lst2.append(l2.val)
            l2 = l2.next
        
        lst1.reverse()
        lst2.reverse()
        longer, shorter = lst1, lst2
        if len(lst1) < len(lst2):
            longer, shorter = shorter, longer
        i = 0
        tmp = 0
        while i < len(shorter):
            longer[i], tmp = (longer[i] + shorter[i] + tmp) % 10, (longer[i] + shorter[i] + tmp) //10
            i += 1
        while i < len(longer):
            longer[i], tmp = (longer[i] + tmp) % 10, (longer[i] + tmp) // 10
            i += 1
        if tmp != 0:
            longer.append(1)
        longer.reverse()
        head = node = ListNode(0)
        for i in range(len(longer)):
            node.next = ListNode(longer[i])
            node = node.next
        return head.next
