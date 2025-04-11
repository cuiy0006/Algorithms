class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        min_val = 0
        res = nums[0]
        for num in nums:
            curr += num
            res = max(res, curr-min_val)
            min_val = min(min_val, curr)
        return res
