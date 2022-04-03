class Node:
    def __init__(self, key, value, freq, l=None, n=None):
        self.key = key
        self.val = value
        self.last = l
        self.next = n
        self.freq = freq
        

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_to_root = {} # 
        self.key_to_node = {}
        self.min_freq = 1
        

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        if self.min_freq == node.freq and node.next == node.last:
            self.min_freq += 1
        
        node.last.next, node.next.last = node.next, node.last
        node.freq += 1
        freq = node.freq
        
        if freq not in self.freq_to_root:
            root = Node(None, None, None)
            root.next, root.last = root, root
            self.freq_to_root[freq] = root
        
        root = self.freq_to_root[freq]
        root.next.last, root.next, node.last, node.next = node, node, root, root.next
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.get(key)
        else:
            if len(self.key_to_node) == self.capacity:
                root = self.freq_to_root[self.min_freq]
                old = root.last
                root.last, old.last.next = old.last, root
                del self.key_to_node[old.key]
            
            self.min_freq = 1
            if 1 not in self.freq_to_root:
                root = Node(None, None, None)
                root.next, root.last = root, root
                self.freq_to_root[1] = root

            root = self.freq_to_root[1]
            new = Node(key, value, 1)
            root.next.last, root.next, new.next, new.last = new, new, root.next, root
            self.key_to_node[key] = new
            
                
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
