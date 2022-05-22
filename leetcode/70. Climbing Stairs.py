class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        last = 2
        lastlast = 1
        
        i = 3
        while i <= n:
            last, lastlast = last + lastlast, last
            i += 1
        
        return last
