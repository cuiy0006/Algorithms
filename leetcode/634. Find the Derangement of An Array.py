class Solution:
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 10**9 + 7
        x,y = 1,0
        for i in range(2, n+1):
            x, y = y, (i-1) * (x+y) % m
        return y
