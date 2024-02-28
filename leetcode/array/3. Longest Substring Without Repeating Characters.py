class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        i = 0
        j = 0
        res = 0

        while j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                j += 1
                res = max(res, j-i)
            else:
                while i < j:
                    if s[i] == s[j]:
                        i += 1
                        break
                    else:
                        visited.remove(s[i])
                        i += 1
                j += 1
        return res