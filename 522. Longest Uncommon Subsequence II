#1
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def isSub(main, sub):
            i = 0
            j = 0
            while i < len(main):
                if main[i] == sub[j]:
                    j += 1
                    if j == len(sub):
                        return 1
                i += 1
            return 0
            
        for sub in sorted(strs, key=len, reverse=True):
            if sum(isSub(main, sub) for main in strs) == 1:
                return len(sub)
        return -1



#2
def findLUSlength1(self, strs):
    def issubsequence(s, t):
        t = iter(t)
        return all(c in t for c in s)
    for s in sorted(strs, key=len, reverse=True):
        if sum(issubsequence(s, t) for t in strs) == 1:
            return len(s)
    return -1
