class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.minval = sys.maxsize

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.minval:
            self.s.append(self.minval)
            self.minval = x
        self.s.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.minval == self.s.pop():
            self.minval = self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval

    
class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(self.curr_min)
        self.stack.append(val)
        self.curr_min = min(self.curr_min, val)

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
