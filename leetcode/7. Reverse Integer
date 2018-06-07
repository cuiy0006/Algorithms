class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_positive = x >= 0
        x = abs(x)
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
        if not is_positive:
            res = -res
        if res < -2147483648 or res > 2147483647:
            return 0
        else:
            return res
