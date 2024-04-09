class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)
        while i < j:
            mid = (i+j) // 2
            if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == len(nums)-1 or nums[mid] > nums[mid+1]):
                return mid
            if mid == 0 or nums[mid] > nums[mid-1]:
                i = mid + 1
            else:
                j = mid
        
        return -1
