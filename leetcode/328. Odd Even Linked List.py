# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddHead = odd = ListNode(0)
        evenHead = even = ListNode(0)
        isOdd = True
        node = head
        while node != None:
            if isOdd:
                odd.next = node
                odd, node = odd.next, node.next
            else:
                even.next = node
                even, node = even.next, node.next
            isOdd = not isOdd
        even.next = None
        odd.next = evenHead.next
        return oddHead.next
