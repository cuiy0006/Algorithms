class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.i = 0
        self.idx = [0, 0]

    def next(self) -> int:
        res = self.v[self.i][self.idx[self.i]]
        self.idx[self.i] += 1
        self.i = (self.i+1) % 2
        return res

    def hasNext(self) -> bool:
        if self.idx[self.i] < len(self.v[self.i]):
            return True
        j = self.i
        self.i = (self.i+1) % 2
        while self.i != j:
            if self.idx[self.i] < len(self.v[self.i]):
                return True
            self.i = (self.i+1)%2
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())



class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v1_idx = 0
        self.v2_idx = 0
        if len(self.v1) == 0:
            self.v1, self.v2 = self.v2, self.v1

    def next(self) -> int:
        val = self.v1[self.v1_idx]
        self.v1_idx += 1
        if self.v2_idx != len(self.v2):
            self.v1, self.v2, self.v1_idx, self.v2_idx = self.v2, self.v1, self.v2_idx, self.v1_idx
        return val

    def hasNext(self) -> bool:
        return not (self.v1_idx == len(self.v1) and self.v2_idx == len(self.v2))


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
