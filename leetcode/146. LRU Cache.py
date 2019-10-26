class ListNode:
    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.root = ListNode(0, 0, None, None)
        self.root.next = self.root
        self.root.prev = self.root
        self.dic = {}
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        node.next.prev, node.prev.next = node.prev, node.next
        self.root.prev.next, self.root.prev, node.next, node.prev = node, node, self.root, self.root.prev
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.get(key)
            return
        
        if len(self.dic) == self.cap:
            remove = self.root.next
            del self.dic[remove.key]
            self.root.next.next.prev, self.root.next = self.root, self.root.next.next
        
        node = ListNode(key, value, self.root, self.root.prev)
        self.dic[key] = node
        self.root.prev.next, self.root.prev = node, node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
