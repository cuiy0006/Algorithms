class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalpha() and not s[i].isnumeric():
                i += 1
            while i < j and not s[j].isalpha() and not s[j].isnumeric():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
