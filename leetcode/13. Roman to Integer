class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        prev = 0
        for c in s:
            if dic[c] > prev:
                res -= 2 * prev
            res += dic[c]
            prev = dic[c]
        return res
