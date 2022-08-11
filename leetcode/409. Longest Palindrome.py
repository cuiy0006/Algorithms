class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        
        res = 0
        for c in dic:
            cnt = dic[c]
            if cnt % 2 == 1:
                res += cnt-1
            else:
                res += cnt
        
        if res < len(s):
            res += 1
        
        return res
        
