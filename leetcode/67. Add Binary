class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        tmp = 0
        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            a += '0' * (len(b) - len(a))
        else:
            b += '0' * (len(a) - len(b))
        for i in range(min(len(a), len(b))):
            if a[i] == '1' and b[i] == '1':
                if tmp == 0:
                    res.append('0')
                else:
                    res.append('1')
                tmp = 1
            elif a[i] == '0' and b[i] == '0':
                if tmp == 0:
                    res.append('0')
                else:
                    res.append('1')
                tmp = 0
            else:
                if tmp == 0:
                    res.append('1')
                    tmp = 0
                else:
                    res.append('0')
                    tmp = 1
        if tmp == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)
