class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[right]:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] > nums[right]:
                    if target > nums[mid] or target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    if target < nums[mid] or target >= nums[left]:
                        right = mid
                    else:
                        left = mid + 1
        
        return left if nums[left] == target else -1






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
