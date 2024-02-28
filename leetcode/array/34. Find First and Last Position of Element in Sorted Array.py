class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            i = 0
            j = len(nums)
            while i < j:
                mid = (i+j) // 2
                if nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid
            if i < len(nums) and nums[i] == target:
                return i
            return -1
        
        def find_last():
            i = 0
            j = len(nums)
            while i < j:
                mid = (i+j) // 2
                if nums[mid] <= target:
                    i = mid + 1
                else:
                    j = mid
            i -= 1
            if i >= 0 and nums[i] == target:
                return i
            return -1

        return [find_first(), find_last()]
