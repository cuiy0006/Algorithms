# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        q = deque([root])
        while len(q) != 0:
            cnt = len(q)
            while cnt != 0:
                node = q.popleft()
                cnt -= 1
                if cnt == 0:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)





# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        curr = root
        next_curr = None
        next_head = None
        
        while curr is not None:
            while curr is not None:
                if curr.left is not None:
                    if next_curr is None:
                        next_head = curr.left
                        next_curr = curr.left
                    else:
                        next_curr.next = curr.left
                        next_curr = next_curr.next
                    
                if curr.right is not None:
                    if next_curr is None:
                        next_head = curr.right
                        next_curr = curr.right
                    else:
                        next_curr.next = curr.right
                        next_curr = next_curr.next
                
                curr = curr.next
            curr = next_head
            next_head = None
            next_curr = None



