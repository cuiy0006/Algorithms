class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            index = t.find(c)
            if index == -1:
                return False
            t = t[index+1:]
        return True
