class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[j] == 2:
                j -= 1
            while i < j and nums[i] != 2:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        
        i = 0
        while i < j:
            while i < j and nums[j] == 1:
                j -= 1
            while i < j and nums[i] == 0:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
