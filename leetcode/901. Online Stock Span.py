class StockSpanner:

    def __init__(self):
        self.stack = [] # (price, day)
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while len(self.stack) != 0 and price >= self.stack[-1][0]:
            self.stack.pop()
        if len(self.stack) == 0:
            res = self.day
        else:
            res = self.day - self.stack[-1][1]
        self.stack.append((price, self.day))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
