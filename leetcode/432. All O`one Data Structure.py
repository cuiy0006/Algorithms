class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.last = None
        self.cnt = 0

class AllOne:

    def __init__(self):
        self.key_to_node = {}
        self.cnt_to_root = {}
        self.max_cnt = 0
        self.min_cnt = 1


    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            self.key_to_node[key] = Node(key)
        else:
            node = self.key_to_node[key]
            node.next.last, node.last.next = node.last, node.next
        node = self.key_to_node[key]
        node.cnt += 1
        
        if node.cnt not in self.cnt_to_root:
            root = self.cnt_to_root[node.cnt] = Node(None)
            root.next, root.last = root, root
        
        root = self.cnt_to_root[node.cnt]
        node.next, node.last = root.next, root
        root.next.last, root.next = node, node
        
        self.max_cnt = max(self.max_cnt, node.cnt)
        self.min_cnt = min(self.min_cnt, node.cnt)
            

    def dec(self, key: str) -> None:
        node = self.key_to_node[key]
        node.cnt -= 1
        node.next.last, node.last.next = node.last, node.next
        if node.cnt == 0:
            del self.key_to_node[key]
        else:
            root = self.cnt_to_root[node.cnt]
            node.next, node.last = root.next, root
            root.next.last, root.next = node, node
            self.min_cnt = min(self.min_cnt, node.cnt)

    def getMaxKey(self) -> str:
        while self.max_cnt in self.cnt_to_root:
            root = self.cnt_to_root[self.max_cnt]
            if root == root.next:
                self.max_cnt -= 1
            else:
                return root.next.key
        self.max_cnt = 0
        return ''
        

    def getMinKey(self) -> str:
        while self.min_cnt in self.cnt_to_root:
            root = self.cnt_to_root[self.min_cnt]
            if root == root.next:
                self.min_cnt += 1
            else:
                return root.next.key
        self.min_cnt = 1
        return ''
            


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
