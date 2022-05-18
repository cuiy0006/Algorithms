class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(idx, curr):
            if idx == len(nums):
                res.append(curr[:])
                return
            
            s = set()
            for i in range(idx, len(nums)):
                if curr[i] in s:
                    continue
                s.add(curr[i])
                curr[idx], curr[i] = curr[i], curr[idx]
                helper(idx+1, curr)
                curr[idx], curr[i] = curr[i], curr[idx]
            
        helper(0, nums)
        return res
