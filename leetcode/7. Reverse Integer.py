class Solution:
    def reverse(self, x: int) -> int:
        isPositive = True
        if x < 0:
            isPositive = False
            x = -x
        res = 0
        while x != 0:
            r = x % 10
            x = x // 10
            res = res * 10 + r
        res = res if isPositive else -res
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res
