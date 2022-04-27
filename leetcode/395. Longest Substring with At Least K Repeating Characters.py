class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(start, end):
            if start > end:
                return 0
            
            res = 0
            counts = [0] * 26
            for i in range(start, end+1):
                counts[ord(s[i])-ord('a')] += 1
            
            i = j = start
            while j <= end:
                if counts[ord(s[j])-ord('a')] < k:
                    res = max(res, helper(i, j-1))
                    i = j + 1
                j += 1
            
            return res
