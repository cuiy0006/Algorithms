class Node:
    def __init__(self, start, end):
        self.left = self.right = None
        self.start = start
        self.end = end

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        
        node = self.root
        while True:
            if start >= node.end:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = Node(start, end)
                    return True
            elif end <= node.start:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = Node(start, end)
                    return True
            else:
                return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
