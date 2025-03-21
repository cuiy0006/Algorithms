class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.start = 0
        self.end = -1
        self.size = 0
        self.arr = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end = (self.end+1) % self.k
        self.arr[self.end] = value
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start+1) % self.k
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.end]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



class MyCircularQueue:

    def __init__(self, k: int):
        self.start = -1
        self.rear = -1
        self.arr = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.start = 0
            self.rear = 0
            self.arr[0] = value
        else:
            self.rear = (self.rear+1)%len(self.arr)
            self.arr[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        is_last_element = (self.start == self.rear)
        # self.arr[self.start] == None
        self.start = (self.start+1)%len(self.arr)
        if is_last_element:
            self.start = -1
            self.rear = -1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.rear == -1

    def isFull(self) -> bool:
        return (self.rear+1)%len(self.arr) == self.start


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
