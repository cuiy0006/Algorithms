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
