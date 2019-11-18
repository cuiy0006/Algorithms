class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = -1
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            for s in strs:
                if len(s) - 1 < i:
                    return '' if idx == -1 else strs[0][:idx+1]
                if s[i] != strs[0][i]:
                    return '' if idx == -1 else strs[0][:idx+1]
            idx = i
        return strs[0]
