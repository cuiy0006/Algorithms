class StockPrice:

    def __init__(self):
        self.ts = 0
        self.ts_to_price = {}
        self.price = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.ts:
            self.ts = timestamp
            self.ts_to_price[timestamp] = price
            self.price.add(price)
        else:
            if timestamp in self.ts_to_price:
                self.price.remove(self.ts_to_price[timestamp])
            self.ts_to_price[timestamp] = price
            self.price.add(price)

    def current(self) -> int:
        return self.ts_to_price[self.ts]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
