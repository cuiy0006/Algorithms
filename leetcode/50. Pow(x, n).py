import sys

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        n_positive = n > 0
        
        n = abs(n)
        
        x_positive = x > 0
        
        x = abs(x)
        
        def helper(n):
            if n == 0:
                return 1
            is_odd = n % 2
            sub = helper(n // 2)
            if sub < 0.000000001:
                return 0
            if sys.maxsize / sub < sub:
                return sys.maxsize
            
            if is_odd:
                return sub * sub * x
            else:
                return sub * sub
        
        res = helper(n)
        
        res = res if n_positive else 1 / res
        
        if x_positive:
            return res
        else:
            return res if n % 2 == 0 else -res
