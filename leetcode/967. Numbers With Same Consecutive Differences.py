class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def dfs(curr, last, d):
            if d == n:
                res.append(curr)
                return
            
            digit = last-k
            if digit >= 0:
                dfs(10*curr+digit, digit, d+1)
            digit = last+k
            if digit <= 9 and digit != last-k:
                dfs(10*curr+digit, digit, d+1)

        for i in range(1, 10):
            dfs(i, i, 1)
        return res

