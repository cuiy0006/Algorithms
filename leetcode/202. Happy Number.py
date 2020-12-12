class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s:
                return False
            else:
                s.add(n)
            new = 0
            while n != 0:
                new += (n % 10) ** 2
                n = n // 10
            n = new
        return True
