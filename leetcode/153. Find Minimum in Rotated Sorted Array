class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] <= nums[-1]:
            return nums[0]
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < nums[-1]:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                else:
                    j = mid
            else:
                i = mid + 1
        return nums[i]
