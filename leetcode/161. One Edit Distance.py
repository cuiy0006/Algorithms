class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        if abs(len(s) - len(t)) > 1:
            return False
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if len(s) > len(t):
                    return s[:i] + s[i+1:] == t
                elif len(s) < len(t):
                    return t[:i] + t[i+1:] == s
                else:
                    return s[i+1:] == t[i+1:]
        return True                   
