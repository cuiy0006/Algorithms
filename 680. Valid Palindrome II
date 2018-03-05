class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isValid(sub):
            i = 0
            j = len(sub) - 1
            while i < j:
                if sub[i] != sub[j]:
                    return False
                i += 1
                j -= 1
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isValid(s[i:j]) or isValid(s[i+1:j+1])
            i += 1
            j -= 1
        return True
