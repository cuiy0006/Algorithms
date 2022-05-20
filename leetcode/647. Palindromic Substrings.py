class Solution:
    def countSubstrings(self, s: str) -> int:
        def cnt_of_palin(i,j):
            cnt = 0
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                cnt += 1
                i -= 1
                j += 1
            return cnt
        
        res = 0
        for i in range(len(s)):
            res += cnt_of_palin(i, i)
            if i > 0:
                res += cnt_of_palin(i-1, i)
        
        return res
