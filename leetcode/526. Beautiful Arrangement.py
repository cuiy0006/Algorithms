class Solution:
    def countArrangement(self, n: int) -> int:
        def get_count(idx, curr):
            if idx == n:
                print(curr)
                return 1
            res = 0
            for i in range(idx, len(curr)):
                curr[i], curr[idx] = curr[idx], curr[i]
                if curr[idx] % (idx+1) == 0 or (idx+1) % curr[idx] == 0:
                   res += get_count(idx+1, curr)
                curr[i], curr[idx] = curr[idx], curr[i]
            return res
        
        return get_count(0, [i for i in range(1, n+1)])

