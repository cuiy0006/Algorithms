class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        num_to_step = {} # num -> step
        res = 0
        
        for num in arr:
            if num - difference in num_to_step:
                step = num_to_step[num-difference] + 1
            else:
                step = 1
            
            res = max(res, step)
            if num not in num_to_step:
                num_to_step[num] = step
            else:
                num_to_step[num] = max(num_to_step[num], step)
        
        return res
        
