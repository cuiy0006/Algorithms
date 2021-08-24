class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.removed = False
        
    def __lt__(self, other):
        if self.val == other.val:
            return self.idx > other.idx
        else:
            return self.val > other.val

from heapq import heappush, heappop

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.idx = 0
        self.heap = []
        self.stack = []
        

    def push(self, x: int) -> None:
        node = Node(x, self.idx)
        self.idx += 1
        self.stack.append(node)
        heappush(self.heap, node)
        

    def pop(self) -> int:
        self.top()
        node = self.stack.pop()
        node.removed = True
        return node.val
        

    def top(self) -> int:
        while True:
            node = self.stack[-1]
            if not node.removed:
                break
            self.stack.pop()
                
        return self.stack[-1].val
        

    def peekMax(self) -> int:
        while True:
            node = self.heap[0]
            if not node.removed:
                break
            heappop(self.heap)
        return node.val
        

    def popMax(self) -> int:
        self.peekMax()
        node = heappop(self.heap)
        node.removed = True
        return node.val
    

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
