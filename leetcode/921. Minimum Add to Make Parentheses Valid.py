class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        
        left = 0
        for c in s:
            if left == 0 and c == ')':
                res += 1
            else:
                if c == '(':
                    left += 1
                else:
                    left -= 1
        
        res += left
        return res
