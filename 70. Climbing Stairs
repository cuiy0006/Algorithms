class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        first = 1
        second = 2
        i = 3
        while i <= n:
            if i == n:
                return first + second
            first, second = second, first + second
            i += 1
