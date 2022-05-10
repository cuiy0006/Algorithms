class Node:
    def __init__(self, val):
        self.children = {}
        self.val = val

class FileSystem:

    def __init__(self):
        self.root = Node(None)
        

    def createPath(self, path: str, value: int) -> bool:
        names = path[1:].split('/')
        node = self.root
        for i in range(len(names)-1):
            if names[i] not in node.children:
                return False
            node = node.children[names[i]]
        if names[-1] in node.children:
            return False
        node.children[names[-1]] = Node(value)
        
        return True
        

    def get(self, path: str) -> int:
        names = path[1:].split('/')
        node = self.root
        for name in names:
            if name not in node.children:
                return -1
            node = node.children[name]
        return node.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
