class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            if nums[i] != sorted_nums[i]:
                break
            i += 1
        
        while j >= i:
            if nums[j] != sorted_nums[j]:
                break
            j -= 1
        
        return j - i + 1
