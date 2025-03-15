class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def traverse(l, r):
            if l >= r:
                return 1
            
            res = 0
            for i in range(l, r+1):
                res += traverse(l, i-1) * traverse(i+1, r)
            return res
        
        return traverse(1, n)



class Solution:
    def numTrees(self, n: int) -> int:
        dp = [None for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        def num_trees(n):
            if dp[n] is not None:
                return dp[n]
            cnt = 0
            for i in range(1, n+1):
                left = i - 1
                right = n - i
                cnt += num_trees(left) * num_trees(right)
            dp[n] = cnt
            return cnt

        return num_trees(n)
