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
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif self.min_stack[-1] >= val:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
