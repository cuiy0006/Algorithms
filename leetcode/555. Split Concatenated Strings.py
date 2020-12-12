class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = None
        strs = [max(s, s[::-1]) for s in strs]
        for i, s in enumerate(strs):
            for split in (s, s[::-1]):
                for j in range(len(split)+1):
                    val = split[j:] + ''.join(strs[i+1:] + strs[:i]) + split[:j]
                    res = max(res, val)
                        
        return res
