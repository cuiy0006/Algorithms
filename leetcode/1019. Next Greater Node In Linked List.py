# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        def traverse(node):
            if node is None:
                return
            traverse(node.next)
            while len(stack) != 0 and node.val >= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                res.append(0)
            else:
                res.append(stack[-1])
            stack.append(node.val)
        
        traverse(head)
        res.reverse()
        return res
