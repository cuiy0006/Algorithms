class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.s = compressedString
        self.idx = 0
        self.curr = ' '
        self.cnt = 0

    def next(self):
        """
        :rtype: str
        """
        if self.cnt != 0:
            self.cnt -= 1
            return self.curr
        else:
            if not self.hasNext():
                return ' '
            else:
                self.curr = self.s[self.idx]
                for i in range(self.idx + 1, len(self.s)):
                    if self.s[i].isdigit():
                        self.cnt = self.cnt * 10 + int(self.s[i])
                    else:
                        self.idx = i
                        break
                    if i == len(self.s) - 1:
                        self.idx = len(self.s)
                        break
                self.cnt -= 1
                return self.curr
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cnt != 0:
            return True
        else:
            if self.idx == len(self.s):
                return False
            else:
                return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
