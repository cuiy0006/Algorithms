class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 1:
            return False
        for i in range(1, n):
            if n // i * i == n:
                if s[:i] * (n//i) == s:
                    return True
        return False
