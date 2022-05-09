class Solution:
    def countArrangement(self, n: int) -> int:
        perm = [i for i in range(n+1)]
        res = 0
        
        def helper(start):
            if start == len(perm):
                nonlocal res
                res += 1
                return
        
            for i in range(start, len(perm)):
                if perm[i] % start != 0 and start % perm[i] != 0:
                    continue
                    
                perm[i], perm[start] = perm[start], perm[i]
                helper(start+1)
                perm[start], perm[i] = perm[i], perm[start]

        helper(1)
        return res
