class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        target = total // 2
        
        nums.sort()
        
        @cache
        def can_part(curr, idx):
            if curr == target:
                return True
            
            if curr > target or idx == len(nums):
                return False
            
            return can_part(curr, idx+1) or can_part(curr+nums[idx], idx+1)
        
        return can_part(0, 0)
