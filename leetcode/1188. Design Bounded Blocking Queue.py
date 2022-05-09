from threading import Condition
from collections import deque

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.cond = Condition()
        self.cap = capacity
        self.q = deque()

    def enqueue(self, element: int) -> None:
        with self.cond:
            self.cond.wait_for(lambda: len(self.q) < self.cap)
            self.q.append(element)
            self.cond.notify()
            
    def dequeue(self) -> int:
        with self.cond:
            self.cond.wait_for(lambda: len(self.q) != 0)
            res = self.q.popleft()
            self.cond.notify()
        return res

    def size(self) -> int:
        return len(self.q)
