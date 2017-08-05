class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == 0 or mid == len(nums) - 1 or nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]
            
            if mid % 2 == 1:
                if nums[mid] == nums[mid + 1]:
                    right = mid - 1    
                elif nums[mid] == nums[mid - 1]:
                    left = mid + 1
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2    
                elif nums[mid] == nums[mid - 1]:
                    right = mid - 2
