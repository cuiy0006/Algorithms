class StockSpanner:

    def __init__(self):
        self.stack = [] # (index, val)
        self.index = 0

    def next(self, price: int) -> int:
        while len(self.stack) and price >= self.stack[-1][1]:
            self.stack.pop()
        start = 0 if len(self.stack) == 0 else self.stack[-1][0]+1
        res = self.index - start + 1
        self.stack.append((self.index, price))
        self.index += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
