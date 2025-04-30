class StockPrice:

    def __init__(self):
        self.ts = 0
        self.ts_to_price = {}
        self.prices = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.ts_to_price:
            self.prices.remove(self.ts_to_price[timestamp])
        self.ts = max(self.ts, timestamp)
        self.ts_to_price[timestamp] = price
        self.prices.add(price)

    def current(self) -> int:
        return self.ts_to_price[self.ts]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]
