class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palin(l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ''
        for i in range(len(s)):
            p = palin(i, i)
            if len(p) > len(res):
                res = p
            if i != 0:
                p = palin(i-1, i)
                if len(p) > len(res):
                    res = p
        
        return res
 