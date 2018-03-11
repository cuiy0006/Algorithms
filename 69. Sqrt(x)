class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <right:
            mid = (left + right)//2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid
            else:
                left = mid + 1
        if left * left > x:
            left -= 1
        return left
