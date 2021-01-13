class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic = {}
        max_len = 0
        i = 0
        
        for j, c in enumerate(s):
            if c in dic:
                dic[c] += 1
                max_len = max(max_len, j - i + 1)
            else:
                dic[c] = 1
                if len(dic) <= k:
                    max_len = max(max_len, j - i + 1)
                else:
                    while i <= j:
                        dic[s[i]] -= 1
                        if dic[s[i]] == 0:
                            del dic[s[i]]
                            i += 1
                            break
                        i += 1
        return max_len
            
