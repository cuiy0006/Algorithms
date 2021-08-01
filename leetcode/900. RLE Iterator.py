class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0

    def next(self, n: int) -> int:
        while self.idx < len(self.encoding):
            cnt = self.encoding[self.idx]
            num = self.encoding[self.idx + 1]
            if cnt == n:
                n = 0
                self.idx += 2
                return num
            elif cnt < n:
                n -= cnt
                self.idx += 2
            else:
                self.encoding[self.idx] -= n
                return num
            
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
