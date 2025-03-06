class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        curr = 1
        for num in nums:
            curr *= num
            res.append(curr)
        
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                res[i] = curr
            else:
                res[i] = curr * res[i-1]
            curr *= nums[i]
        return res


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
