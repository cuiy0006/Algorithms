class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        def isSame(d1, d2):
            for k,v in d1.items():
                if k not in d2 or v != d2[k]:
                    return False
            return True
        
        dic = {}
        for c in s1:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        window = {}
        for i in range(len(s1)):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1
        if isSame(dic, window):
            return True
        for i in range(len(s1), len(s2)):
            window[s2[i - len(s1)]] -= 1
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1
            if isSame(dic, window):
                return True
            
        return False
