class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            while num != None and num >= 1 and num <= len(nums):
                nums[num-1], num = None, nums[num-1]
        
        for i, num in enumerate(nums):
            if num != None:
                return i+1
        return len(nums)+1
