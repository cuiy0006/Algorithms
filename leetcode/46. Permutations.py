class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def get_permute(idx, curr):
            if idx == len(nums):
                res.append(curr[:])
                return
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                nums[i], nums[idx] = nums[idx], nums[i]
                get_permute(idx+1, curr)
                nums[i], nums[idx] = nums[idx], nums[i]
                curr.pop()
            
        get_permute(0, [])
        return res
