class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        for i in range(len(strs[0])):
            c = strs[0][i]
            advance = True
            for word in strs:
                if len(word)-1 < i or word[i] != c:
                    advance = False
                    break
            if not advance:
                break
            idx += 1
        return strs[0][:idx]
