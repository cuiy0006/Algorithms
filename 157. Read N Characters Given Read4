# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        buff = [None] * 4
        cnt = n // 4
        remain = n % 4
        for i in range(cnt):
            tmp = read4(buff)
            for j in range(tmp):
                buf[index] = buff[j]
                index += 1
            if tmp < 4:
                return index
        tmp = read4(buff)
        for i in range(min(tmp, remain)):
            buf[index] = buff[i]
            index += 1
        
        return index
