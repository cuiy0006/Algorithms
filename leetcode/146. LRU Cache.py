class Node:
    def __init__(self, key, val, n=None, l=None):
        self.key = key
        self.val = val
        self.next = n
        self.last = l
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.root = Node(None, None)
        self.root.last = self.root.next = self.root 
        self.dic = {} # key -> node
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        node.last.next, node.next.last = node.next, node.last
        self.root.next.last, self.root.next, node.next, node.last = node, node, self.root.next, self.root
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].val = value
            self.get(key)
        else:
            if len(self.dic) == self.capacity:
                old = self.root.last
                self.root.last, old.last.next = old.last, self.root
                del self.dic[old.key]
            
            new = Node(key, value)
            self.dic[key] = new
            self.root.next.last, self.root.next, new.next, new.last = new, new, self.root.next, self.root 
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
