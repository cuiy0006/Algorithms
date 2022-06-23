class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        
        while i < len(nums):
            while i < len(nums) and nums[i] == val:
                i += 1
            
            if i == len(nums):
                break
            
            nums[j] = nums[i]
            j += 1
            i += 1
        return j
                
                



class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] != val:
                i += 1
            while i < j and nums[j] == val:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] != val:
            return i + 1
        else:
            return i
