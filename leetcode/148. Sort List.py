# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def helper(node):
            if node == None or node.next == None:
                return (node, node)
            
            lleft = lright = ListNode()
            rleft = rright = ListNode()
            
            last = None
            slow = fast = node
            while True:
                if fast == None or fast.next == None:
                    last.next = slow.next
                    last = slow
                    break
                    
                fast = fast.next.next
                last = slow
                slow = slow.next
            
            mleft = mright = last
            p = node
            
            while p != None:
                if p.val == mleft.val:
                    mright.next = p
                    mright = mright.next
                elif p.val > mleft.val:
                    rright.next = p
                    rright = rright.next
                else:
                    lright.next = p
                    lright = lright.next
                p = p.next
            
            mright.next = lright.next = rright.next = None
            
            lleft, lright = helper(lleft.next)
            rleft, rright = helper(rleft.next)
            
            left = lleft
            if lleft == None:
                left = mleft
            else:
                lright.next = mleft
            
            mright.next = rleft
            right = rright if rright != None else mright
            return (left, right)
        
        return helper(head)[0]

























# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        pivot = head.val
        left = l = ListNode(0)
        right = r = ListNode(0)
        mid = m = head
        node = head.next
        
        while node is not None:
            if node.val == pivot:
                m.next, m = node, node
            elif node.val < pivot:
                l.next, l = node, node
            else:
                r.next, r = node, node
            node.next, node = None, node.next
        left = self.sortList(left.next)
        right = self.sortList(right.next)
        m.next = right
        l = left
        while l is not None:
            if l.next is None:
                break
            l = l.next
        if left is None:
            return mid
        else:
            l.next = mid
            return left
        
            
