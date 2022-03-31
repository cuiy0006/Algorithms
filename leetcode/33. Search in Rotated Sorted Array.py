class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] > target or (nums[0] > nums[-1] and nums[mid] <= nums[-1]):
                    j = mid
                else:
                    i = mid + 1
            else:
                if nums[mid] < target or (nums[0] > nums[-1] and nums[mid] >= nums[0]):
                    i = mid + 1
                else:
                    j = mid
        
        return -1
