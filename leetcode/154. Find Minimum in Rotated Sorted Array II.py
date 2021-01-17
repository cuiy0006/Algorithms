class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        i = 0
        j = len(nums) - 1
        while i != j and nums[i] == nums[j]:
            i += 1
        
        while i < j:
            mid = (i + j) // 2
            if nums[mid] >= nums[i] and nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        return nums[i]
