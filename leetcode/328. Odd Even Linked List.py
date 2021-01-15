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

    
    
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        is_even = True
        even = ListNode()
        odd = ListNode()
        e = even
        o = odd
        p = head
        
        while p != None:
            e.next, o.next = p, p.next
            e = e.next
            o = o.next
            if p.next == None:
                break
            p = p.next.next
            
        e.next = odd.next    
        return even.next
