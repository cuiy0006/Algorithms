#1. whitespace
#2. +/-
#3. max int, min int


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        res = 0
        pre = '+'
        for i,c in enumerate(str):
            if i == 0 and (c == '+' or c == '-'):
                pre = c
            elif ord(c) - ord('0') > 9 or ord(c) - ord('0') < 0:
                break
            else:
                num = ord(c) - ord('0')
                res = res * 10 + num
        if pre == '+':
            if res <= 2147483647:
                return res
            else:
                return 2147483647
        else:
            if res <= 2147483648:
                return -res
            else:
                return -2147483648
