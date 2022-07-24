class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def helper(n):
            if n == 1:
                return 1
            res = 1
            for i in range(1, n):
                res = max(res, helper(n-i)*i, (n-i)*i)
            return res
        
        return helper(n)
