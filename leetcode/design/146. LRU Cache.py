class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.last = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.root = Node(None, None)
        self.root.next, self.root.last = self.root, self.root


    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        node.next.last, node.last.next = node.last, node.next
        node.next, node.last, self.root.last.next, self.root.last = self.root, self.root.last, node, node
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.get(key)
            self.dic[key].val = value
            return

        if len(self.dic) == self.cap:
            del_node = self.root.next
            self.root.next, del_node.next.last = del_node.next, self.root
            del self.dic[del_node.key]

        node = Node(key, value)
        self.dic[key] = node
        node.next, node.last, self.root.last.next, self.root.last = self.root, self.root.last, node, node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)