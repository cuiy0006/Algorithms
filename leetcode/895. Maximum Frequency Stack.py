class Node:
    def __init__(self, val):
        self.val = val
        self.freq = 1
        self.next = None
        self.last = None
        self.seq_next = None

class FreqStack:

    def __init__(self):
        self.freq_to_root = {}
        self.val_to_node = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.val_to_node:
            node = self.val_to_node[val] = Node(val)
        else:
            old_node = self.val_to_node[val]
            node = Node(val)
            node.seq_next = old_node
            self.val_to_node[val] = node
            node.freq = old_node.freq + 1
            
        freq = node.freq
        self.max_freq = max(self.max_freq, freq)
        if freq not in self.freq_to_root:
            root = self.freq_to_root[freq] = Node(None)
            root.next, root.last = root, root
        else:
            root = self.freq_to_root[freq]
        root.last.next, root.last, node.last, node.next = node, node, root.last, root
            
    def pop(self) -> int:
        root = self.freq_to_root[self.max_freq]
        node = root.last
        node.next.last, node.last.next = node.last, node.next
        res = node.val
        
        old_node = node.seq_next
        if old_node is None:
            del self.val_to_node[node.val]
        else:
            self.val_to_node[node.val] = old_node
        
        while root.last == root:
            self.max_freq -= 1
            if self.max_freq == 0:
                break
            root = self.freq_to_root[self.max_freq]
        return res
        

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
