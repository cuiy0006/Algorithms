from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.right) != 0 and num >= self.right[0]:
            if len(self.right) > len(self.left):
                heappush(self.left, -heappop(self.right))
            heappush(self.right, num)
        elif len(self.left) != 0 and num <= -self.left[0]:
            if len(self.left) > len(self.right):
                heappush(self.right, -heappop(self.left))
            heappush(self.left, -num)
        else:
            if len(self.left) < len(self.right):
                heappush(self.left, -num)
            else:
                heappush(self.right, num)
            

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
