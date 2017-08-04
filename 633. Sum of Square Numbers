class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(0, int(c**0.5) + 1):
            b = int((c - a ** 2) ** 0.5)
            if b ** 2 + a ** 2 == c:
                return True
        return False
