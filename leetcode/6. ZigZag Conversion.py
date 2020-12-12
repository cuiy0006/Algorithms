class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        distance = (numRows - 1) * 2
        res = ''
        i = 0
        while i < len(s):
            res += s[i]
            i += distance
        for j in range(1, numRows-1):
            i = j
            while i < len(s):
                res += s[i]
                if i + distance - 2*j < len(s):
                    res += s[i + distance - 2*j]
                i += distance
        i = numRows-1
        while i < len(s):
            res += s[i]
            i += distance
        return res
