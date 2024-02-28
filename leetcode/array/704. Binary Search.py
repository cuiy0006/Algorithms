class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        
        if i < len(nums) and nums[i] == target:
            return i
        return -1
