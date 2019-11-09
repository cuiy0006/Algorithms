class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isPositive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            val = divisor
            amount = 1
            while val < dividend:
                tmp = val << 1
                if tmp >= dividend:
                    break
                val = tmp
                amount = amount << 1
            dividend -= val
            res += amount
        if not isPositive:
            res = -res
        return min(res, 2**31-1)
