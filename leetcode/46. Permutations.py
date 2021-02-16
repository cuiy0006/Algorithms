class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(k, curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(k, len(nums)):
                nums[i], nums[k] = nums[k], nums[i]
                curr.append(nums[k])
                helper(k+1, curr)
                curr.pop()
                nums[k], nums[i] = nums[i], nums[k]
        
        helper(0, [])
        return res
