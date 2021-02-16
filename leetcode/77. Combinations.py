class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(m, curr):
            if len(curr) == k:
                res.append(curr[:])
                return
            
            for i in range(m, n+1):
                curr.append(i)
                helper(i+1, curr)
                curr.pop()
                
        helper(1, [])
        return res
