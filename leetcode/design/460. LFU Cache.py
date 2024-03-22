class Node:
    def __init__(self, key, value, freq):
        self.key = key
        self.val = value
        self.next = None
        self.last = None
        self.freq = freq


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_node = {}
        self.freq_root = {}
        self.min_freq = 1


    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        freq = node.freq + 1
        node.next.last, node.last.next = node.last, node.next
        if self.min_freq == node.freq and self.freq_root[node.freq].next == self.freq_root[node.freq]:
            self.min_freq = freq

        if freq not in self.freq_root:
            root = Node(None, None, None)
            root.next, root.last = root, root
            self.freq_root[freq] = root

        root = self.freq_root[freq]
        node.freq += 1
        root.last.next, root.last, node.next, node.last = node, node, root, root.last
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            self.get(key)
            self.key_node[key].val = value
            return

        if len(self.key_node) == self.cap:
            del_node = self.freq_root[self.min_freq].next
            del_node.next.last, del_node.last.next = del_node.last, del_node.next
            del self.key_node[del_node.key]
        
        self.min_freq = 1
        node = Node(key, value, 1)
        self.key_node[key] = node

        if 1 not in self.freq_root:
            root = Node(None, None, None)
            root.next, root.last = root, root
            self.freq_root[1] = root
        root = self.freq_root[1]
        root.last.next, root.last, node.next, node.last = node, node, root, root.last


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)