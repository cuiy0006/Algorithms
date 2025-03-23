class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.next = None
        self.down = None

class FreqStack:

    def __init__(self):
        self.head = Node(None, 0)
        self.tail = self.head
        self.freq_to_root = {0: self.head}
        self.val_to_nodes = {}

    def push(self, val: int) -> None:
        if val not in self.val_to_nodes:
            self.val_to_nodes[val] = []
        freq = len(self.val_to_nodes[val]) + 1
        node = Node(val, freq)
        self.val_to_nodes[val].append(node)
        if freq not in self.freq_to_root:
            root = Node(None, freq)
            self.freq_to_root[freq] = root
            self.tail = root
            root.down = self.freq_to_root[freq-1]
        root = self.freq_to_root[freq]
        root.next, node.next = node, root.next

    def pop(self) -> int:
        node = self.tail.next
        self.tail.next = node.next
        if self.tail.next is None:
            del self.freq_to_root[self.tail.freq]
            self.tail = self.tail.down
        self.val_to_nodes[node.val].pop()
        return node.val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
