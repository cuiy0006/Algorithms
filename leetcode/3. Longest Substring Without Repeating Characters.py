class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        j = 0
        res = 0
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
            else:
                res = max(res, len(seen))
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                i += 1
            j += 1
        res = max(res, len(seen))
        return res
