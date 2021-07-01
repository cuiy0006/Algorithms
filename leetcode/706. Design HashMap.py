class Node:
    def __init__(self, key, val, next_node=None):
        self.key = key
        self.val = val
        self.next = next_node
    

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1024
        self.arr = [Node(None, None) for i in range(self.size)]
        
    
    def hash(self, key):
        return key % self.size 
    

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.hash(key)
        root = self.arr[bucket]
        last = root
        node = root.next
        
        while node is not None and node.key != key:
            last = node
            node = node.next

        if node is None:
            last.next = Node(key, value)
        else:
            node.val = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self.hash(key)
        root = self.arr[bucket]
        node = root.next
        
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return -1
        else:
            return node.val
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.hash(key)
        root = self.arr[bucket]
        last = root
        node = root.next
        
        while node is not None and node.key != key:
            last = node
            node = node.next
            
        if node is not None:
            last.next = node.next
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
