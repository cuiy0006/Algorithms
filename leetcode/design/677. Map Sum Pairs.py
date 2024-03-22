class Node:
    def __init__(self):
        self.children = {}
        self.prefix_val = 0
        self.end_val = 0


class MapSum:

    def __init__(self):
        self.root =  Node()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            if c not in node.children:
                node = None
                break
            node = node.children[c]
        end_val = 0 if node is None else node.end_val
        prefix_val = val - end_val

        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.prefix_val += prefix_val
        node.end_val = val


    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.prefix_val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)