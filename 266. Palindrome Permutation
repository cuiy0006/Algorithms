class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        
        odd = 0
        for _, cnt in dic.items():
            if cnt % 2 != 0:
                odd += 1
                if odd > 1:
                    return False
        return True
