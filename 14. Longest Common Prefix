class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        for i in range(1, len(strs[0])+1):
            prefix = strs[0][:i]
            for s in strs:
                if s[:i] != prefix:
                    return s[:i-1]
        return strs[0]
