class HitCounter:

    def __init__(self):
        self.cnt = 0
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.cnt += 1
        if len(self.q) != 0 and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        while len(self.q) != 0 and self.q[0][0]+300 <= timestamp:
            [_, cnt] = self.q.popleft()
            self.cnt -= cnt
        return self.cnt


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
