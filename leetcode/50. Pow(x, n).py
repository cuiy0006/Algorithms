class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            m = n // 2
            d = n % 2
            part = helper(m)
            res = part * part
            if d == 1:
                res = res * x
            return res

        if n < 0:
            return 1 / helper(-n)
        else:
            return helper(n)