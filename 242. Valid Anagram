class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = [0 for i in range(26)]
        for c in s:
            dic[ord(c)-ord('a')] += 1
        for c in t:
            if dic[ord(c)-ord('a')] > 0:
                dic[ord(c)-ord('a')] -= 1
            else:
                return False
        return True
