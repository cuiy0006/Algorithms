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


class StockPrice:

    def __init__(self):
        self.ts = 0
        self.ts_to_price = {}
        self.max_h = []
        self.min_h = []

    def update(self, timestamp: int, price: int) -> None:
        self.ts = max(self.ts, timestamp)
        self.ts_to_price[timestamp] = price
        heappush(self.max_h, (-price, timestamp))
        heappush(self.min_h, (price, timestamp))

    def current(self) -> int:
        return self.ts_to_price[self.ts]

    def maximum(self) -> int:
        while len(self.max_h) != 0:
            price, ts = self.max_h[0]
            if self.ts_to_price[ts] != -price:
                heappop(self.max_h)
            else:
                return -price
        return -1

    def minimum(self) -> int:
        while len(self.min_h) != 0:
            price, ts = self.min_h[0]
            if self.ts_to_price[ts] != price:
                heappop(self.min_h)
            else:
                return price
        return -1
