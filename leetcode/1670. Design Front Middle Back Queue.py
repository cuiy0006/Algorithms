class FrontMiddleBackQueue:

    def __init__(self):
        self.first = deque()
        self.second = deque()

    def pushFront(self, val: int) -> None:
        self.first.appendleft(val)
        if len(self.first) > len(self.second)+1:
            self.second.appendleft(self.first.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.first) == len(self.second):
            self.first.append(val)
        else:
            self.second.appendleft(self.first.pop())
            self.first.append(val)

    def pushBack(self, val: int) -> None:
        self.second.append(val)
        if len(self.second) > len(self.first):
            self.first.append(self.second.popleft())

    def popFront(self) -> int:
        if len(self.first) == 0 and len(self.second) == 0:
            return -1
        val = self.first.popleft()
        if len(self.second) > len(self.first):
            self.first.append(self.second.popleft())
        return val

    def popMiddle(self) -> int:
        if len(self.first) == 0 and len(self.second) == 0:
            return -1
        val = self.first.pop()
        if len(self.second) > len(self.first):
            self.first.append(self.second.popleft())
        return val

    def popBack(self) -> int:
        if len(self.first) == 0 and len(self.second) == 0:
            return -1
        if len(self.first) > len(self.second):
            self.second.appendleft(self.first.pop())
        val = self.second.pop()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
