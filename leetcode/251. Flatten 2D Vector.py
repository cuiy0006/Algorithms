class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.i = 0
        self.j = 0
        self.v = v
        while self.i < len(v) and len(v[self.i]) == 0:
            self.i += 1

    def next(self) -> int:
        res = self.v[self.i][self.j]
        if self.j == len(self.v[self.i]) - 1:
            self.j = 0
            self.i += 1
            while self.i < len(self.v) and len(self.v[self.i]) == 0:
                self.i += 1
        else:
            self.j += 1
        return res
        

    def hasNext(self) -> bool:
        i, j, v = self.i, self.j, self.v
        if i >= len(v) or j >= len(v[i]):
            return False
        return True


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
