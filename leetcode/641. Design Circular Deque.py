class MyCircularDeque:

    def __init__(self, k: int):
        self.start = -1
        self.rear = -1
        self.size = 0
        self.arr = [None] * k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.start == -1:
            self.start = 0
            self.rear = 0
            self.arr[0] = value
        else:
            self.start = (self.start-1+len(self.arr)) % len(self.arr)
            self.arr[self.start] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.rear == -1:
            self.start = 0
            self.rear = 0
            self.arr[0] = value
        else:
            self.rear = (self.rear+1) % len(self.arr)
            self.arr[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start+1) % len(self.arr)
        self.size -= 1
        if self.size == 0:
            self.start = -1
            self.rear = -1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear-1+len(self.arr)) % len(self.arr)
        self.size -= 1
        if self.size == 0:
            self.start = -1
            self.rear = -1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.start]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.arr)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
