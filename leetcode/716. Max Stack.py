from sortedcontainers import SortedDict

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.last = None
        

class MaxStack:

    def __init__(self):
        self.dic = SortedDict()
        self.root = Node()
        self.root.last, self.root.next = self.root, self.root
        

    def push(self, x: int) -> None:
        if x not in self.dic:
            self.dic[x] = []
        node = Node(x)
        self.root.next.last, self.root.next, node.last, node.next = node, node, self.root, self.root.next
        self.dic[x].append(node)
        

    def pop(self) -> int:
        node = self.root.next
        node.next.last, node.last.next = node.last, node.next
        node_lst = self.dic[node.val]
        node_lst.pop()
        if len(node_lst) == 0:
            self.dic.pop(node.val)
        return node.val
    

    def top(self) -> int:
        return self.root.next.val
        

    def peekMax(self) -> int:
        return self.dic.peekitem()[0]


    def popMax(self) -> int:
        val, node_lst = self.dic.peekitem()
        node = node_lst.pop()
        if len(node_lst) == 0:
            self.dic.pop(val)
        node.next.last, node.last.next = node.last, node.next
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
