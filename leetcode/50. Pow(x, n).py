class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            tmp = helper(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            else:
                return tmp * tmp * x
        return helper(x, n)
