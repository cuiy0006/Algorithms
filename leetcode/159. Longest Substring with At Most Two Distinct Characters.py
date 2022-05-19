class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        k = 2
        dic = {}
        
        res = 0
        i = 0
        j = 0
        while j < len(s):
            if s[j] in dic:
                dic[s[j]] += 1
            else:
                dic[s[j]] = 1
                if len(dic) == k+1:
                    res = max(res, j-i)
                    while i < j:
                        dic[s[i]] -= 1
                        if dic[s[i]] == 0:
                            del dic[s[i]]
                            i += 1
                            break
                        i += 1
            j += 1
        
        res = max(res, j-i)
        return res
