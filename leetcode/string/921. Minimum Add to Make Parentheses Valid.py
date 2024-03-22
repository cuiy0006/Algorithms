class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        res = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                if left == 0:
                    res += 1
                else:
                    left -= 1
        return res + left
