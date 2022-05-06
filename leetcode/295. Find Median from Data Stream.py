from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.sh = []
        self.lh = []
        

    def addNum(self, num: int) -> None:
        if len(self.sh) == len(self.lh):
            heappush(self.lh, -num)
            heappush(self.sh, -heappop(self.lh))
        else:
            heappush(self.sh, num)
            heappush(self.lh, -heappop(self.sh))
        

    def findMedian(self) -> float:
        if len(self.sh) == len(self.lh):
            return (self.sh[0] - self.lh[0]) / 2
        else:
            return self.sh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
