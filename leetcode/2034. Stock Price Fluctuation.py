class Node:
    def __init__(self, ts, price):
        self.ts = ts
        self.price = price
        self.is_valid = True
        
    def __eq__(self, other):
        return self.price == other.price

class MinNode(Node):
    def __lt__(self, other):
        return self.price < other.price

class MaxNode(Node):
    def __lt__(self, other):
        return self.price > other.price

from heapq import heappush, heappop

class StockPrice:

    def __init__(self):
        self.ts_to_stock = {}
        self.max_h = []
        self.min_h = []
        self.ts = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.ts_to_stock:
            min_node, max_node = self.ts_to_stock[timestamp]
            min_node.is_valid = False
            max_node.is_valid = False
        min_node = MinNode(timestamp, price)
        max_node = MaxNode(timestamp, price)
        heappush(self.max_h, max_node)
        heappush(self.min_h, min_node)
        
        self.ts_to_stock[timestamp] = (min_node, max_node)
        self.ts = max(self.ts, timestamp)

    def current(self) -> int:
        min_node, max_node = self.ts_to_stock[self.ts]
        return min_node.price

    def maximum(self) -> int:
        max_node = self.max_h[0]
        while not max_node.is_valid:
            heappop(self.max_h)
            max_node = self.max_h[0]
        return max_node.price

    def minimum(self) -> int:
        min_node = self.min_h[0]
        while not min_node.is_valid:
            heappop(self.min_h)
            min_node = self.min_h[0]
        return min_node.price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
