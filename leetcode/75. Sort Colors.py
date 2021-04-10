class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] == 0:
                left += 1
            while left < right and nums[right] != 0:
                right -= 1
            
            nums[left], nums[right] = nums[right], nums[left]
        
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] == 1:
                left += 1
            while left < right and nums[right] == 2:
                right -= 1
                
            nums[left], nums[right] = nums[right], nums[left]
            
