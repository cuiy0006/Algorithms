class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        dic = {}
        res = 0
        while j < len(s):
            if s[j] not in dic:
                dic[s[j]] = 0
            dic[s[j]] += 1
            max_cnt = max(dic.values())
            while j-i+1 > max_cnt+k:
                dic[s[i]] -= 1
                i += 1
                max_cnt = max(dic.values())
            res = max(res, j-i+1)
            j += 1
        return res
