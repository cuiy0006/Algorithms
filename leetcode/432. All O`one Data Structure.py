class Node:
    def __init__(self, key):
        self.key = key
        self.cnt = 0
        self.next = None
        self.last = None
        

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt_to_nodes = {}
        self.key_to_node = {}
        self.min_cnt = 1
        self.max_cnt = 1
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.key_to_node:
            self.key_to_node[key] = Node(key)
        node = self.key_to_node[key]
        
        if node.cnt != 0:
            node.next.last, node.last.next = node.last, node.next
        
        node.cnt += 1
            
        if node.cnt not in self.cnt_to_nodes:
            root = Node(None)
            root.next, root.last = root, root
            self.cnt_to_nodes[node.cnt] = root
        root = self.cnt_to_nodes[node.cnt]
                    
        root.next.last, root.next, node.next, node.last = node, node, root.next, root
        
        self.max_cnt = max(self.max_cnt, node.cnt)
        self.min_cnt = min(self.min_cnt, node.cnt)
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        node = self.key_to_node[key]
        node.next.last, node.last.next = node.last, node.next
        
        node.cnt -= 1
        if node.cnt != 0:
            root = self.cnt_to_nodes[node.cnt]
            root.next.last, root.next, node.next, node.last = node, node, root.next, root
            self.min_cnt = min(self.min_cnt, node.cnt)
        else:
            del self.key_to_node[key]
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        while self.max_cnt in self.cnt_to_nodes:
            root = self.cnt_to_nodes[self.max_cnt]
            if root.next != root:
                return root.next.key
            else:
                self.max_cnt -= 1
        return ""
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        while self.min_cnt in self.cnt_to_nodes:
            root = self.cnt_to_nodes[self.min_cnt]
            if root.next != root:
                return root.next.key
            else:
                self.min_cnt += 1
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
