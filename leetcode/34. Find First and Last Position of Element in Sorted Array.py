class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        def findFirst(nums):
            i = 0
            j = len(nums)
            while i < j:
                mid = (i + j) // 2
                if nums[mid] >= target:
                    j = mid
                else:
                    i = mid + 1
            return j
        
        def findLast(nums):
            i = 0
            j = len(nums)
            while i < j:
                mid = (i + j) // 2
                print(mid, i, j)
                if nums[mid] > target:
                    j = mid
                else:
                    i = mid + 1
            return j
        start = findFirst(nums)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = findLast(nums) - 1
        return [start, end]
