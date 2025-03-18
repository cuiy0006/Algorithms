# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.secondlast = deque([root])
        self.last = deque()
        q = deque([root])
        while len(q) != 0:
            size = len(q)
            end = False
            for _ in range(size):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                else:
                    end = True
                if node.right is not None:
                    q.append(node.right)
                else:
                    end = True
            if end:
                break
            self.secondlast = q.copy()

    def insert(self, val: int) -> int:
        added = None
        while len(self.secondlast) != 0:
            size = len(self.secondlast)
            for _ in range(size):
                node = self.secondlast[0]
                if node.left is None:
                    node.left = TreeNode(val)
                    added = node
                elif node.right is None:
                    node.right = TreeNode(val)
                    added = node
                if node.left is not None and node.right is not None:
                    node = self.secondlast.popleft()
                    self.last.append(node.left)
                    self.last.append(node.right)
                if added is not None:
                    break
            if len(self.secondlast) == 0:
                self.secondlast = self.last
                self.last = deque()
            if added is not None:
                break
            
        return added.val
                

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
