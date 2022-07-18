class Solution:
    def largestVariance(self, s: str) -> int:
        char_set = set(s)
        res = 0
        
        for c1 in char_set:
            for c2 in char_set:
                if c1 == c2:
                    continue
                
                lst = []
                for c in s:
                    if c == c1:
                        lst.append(1)
                    elif c == c2:
                        lst.append(-1)
                
                prefix_sum = 0
                curr_min = 0
                curr_min_idx = -1
    
                for i, val in enumerate(lst):
                    prefix_sum += val
                    if prefix_sum < curr_min:
                        curr_min = prefix_sum
                        curr_min_idx = i

                    res = max(res, min(prefix_sum-curr_min, i-curr_min_idx-1))
        
        return res
