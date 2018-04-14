class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums)
        while i < j:
            mid = (i+j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] >= nums[0] and target <= nums[-1] and nums[-1] < nums[0]:
                    i = mid + 1
                else:
                    j = mid
            else:
                if nums[mid] <= nums[-1] and target >= nums[0] and nums[-1] < nums[0]:
                    j = mid
                else:
                    i = mid + 1
        return -1
