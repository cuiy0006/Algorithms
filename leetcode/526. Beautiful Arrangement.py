class Solution:
    def countArrangement(self, n: int) -> int:
        def get_count(idx, curr):
            if idx == n:
                return 1
            res = 0
            for i in range(idx, len(curr)):
                if curr[i] % (idx+1) == 0 or (idx+1) % curr[i] == 0:
                    curr[i], curr[idx] = curr[idx], curr[i]
                    res += get_count(idx+1, curr)
                    curr[i], curr[idx] = curr[idx], curr[i]
            return res
        
        return get_count(0, [i for i in range(1, n+1)])

