class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(start, end):
            dic = {}
            for i in range(start, end+1):
                if s[i] not in dic:
                    dic[s[i]] = 0
                dic[s[i]] += 1

            i = start
            res = 0
            for j in range(start, end+1):
                if dic[s[j]] < k:
                    res = max(res, helper(i, j-1))
                    i = j+1

            if i == start:
                return end-start+1
            res = max(res, helper(i, end))
            return res

        return helper(0, len(s)-1)
