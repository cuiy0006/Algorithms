# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buffer = [None] * 4
        self.pointer = 0
        self.readcnt = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        curr = 0
        while curr < n:
            if self.pointer == 0:
                self.readcnt = read4(self.buffer)
                if self.readcnt == 0:
                    break
            while curr < n and self.pointer < self.readcnt:
                buf[curr] = self.buffer[self.pointer]
                curr += 1
                self.pointer += 1
            if self.pointer >= self.readcnt:
                self.pointer = 0
        return curr
