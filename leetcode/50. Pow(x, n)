class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow(x, n):
            if n == 0:
                return 1
            tmp = pow(x, n//2)
            if n % 2 == 0:
                return tmp * tmp
            else:
                return x * tmp * tmp
        if n >= 0:
            return pow(x, n)
        else:
            return 1/pow(x, -n)
