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
