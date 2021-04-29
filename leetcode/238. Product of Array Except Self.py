class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        res = []
        for num in nums:
            res.append(curr)
            curr *= num
        
        curr = 1
        i = len(nums) - 1
        while i >= 0:
            res[i] = curr * res[i]
            curr *= nums[i]
            i -= 1
        
        return res
