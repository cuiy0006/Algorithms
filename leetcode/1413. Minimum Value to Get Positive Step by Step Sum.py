class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = nums[0]
        
        curr = 0
        for num in nums:
            curr += num
            min_val = min(min_val, curr)

        return max(1 - min_val, 1)
