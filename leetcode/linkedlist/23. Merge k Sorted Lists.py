# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: Self):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
    
    def __eq__(self, other):
        return self.node.val == other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode()
        p = dummy
        for head in lists:
            if head is not None:
                heappush(h, NodeWrapper(head))

        while len(h) != 0:
            node_wrapper = heappop(h)
            node = node_wrapper.node
            p.next = node
            p = p.next
            node = node.next
            if node is None:
                continue
            heappush(h, NodeWrapper(node))

        return dummy.next
