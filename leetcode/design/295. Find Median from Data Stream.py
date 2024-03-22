class MedianFinder:

    def __init__(self):
        self.higher = []
        self.lower = []


    def addNum(self, num: int) -> None:
        if len(self.lower) == 0:
            heappush(self.lower, -num)
        elif len(self.higher) == len(self.lower):
            if num > self.higher[0]:
                heappush(self.lower, -heappop(self.higher))
                heappush(self.higher, num)
            else:
                heappush(self.lower, -num)
        elif len(self.higher) < len(self.lower):
            if num < -self.lower[0]:
                heappush(self.higher, -heappop(self.lower))
                heappush(self.lower, -num)
            else:
                heappush(self.higher, num)
        

    def findMedian(self) -> float:
        if len(self.higher) == len(self.lower):
            return (self.higher[0] - self.lower[0]) / 2
        else:
            return -self.lower[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()