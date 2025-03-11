class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        curr = 0
        for c in s:
            if c == '(':
                if curr < 0:
                    if curr % 2 == 0:
                        res += (-curr) // 2
                    else:
                        res += (-curr+1) // 2 + 1
                    curr = 0
                elif curr % 2 == 1:
                    res += 1
                    curr -= 1
                curr += 2
            else:
                curr -= 1

        if curr < 0:
            if curr % 2 == 0:
                res += (-curr) // 2
            else:
                res += (-curr+1) // 2 + 1
            curr = 2
        else:
            res += curr
        return res






class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        cnt = 0
        
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                left += 1
                i += 1
            else:
                if i == len(s) - 1 or s[i+1] != ')':
                    cnt += 1
                    i += 1
                else:
                    i += 2
                
                if left == 0:
                    cnt += 1
                else:
                    left -= 1
        
        return cnt + left * 2
