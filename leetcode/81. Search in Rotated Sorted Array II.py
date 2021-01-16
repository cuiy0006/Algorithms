class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        
        left = 0
        right = len(nums) - 1
        
        while left != len(nums) - 1 and nums[left] == nums[-1]:
            left += 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[right]:
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
        
        return nums[left] == target
                    
