class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        right = 0
        res = 0
        for c in s:
            if c == '(':
                if right == 1:
                    res += 1
                    left -= 1
                    right = 0
                left += 1
            elif c == ')':
                if left == 0:
                    res += 1
                    left += 1
                if right == 0:
                    right += 1
                else:
                    left -= 1
                    right = 0
        if right == 1:
            res += 1
            left -= 1
        res += left * 2
        return res
