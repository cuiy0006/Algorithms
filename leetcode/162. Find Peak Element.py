class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if (i == 0 or num > nums[i- 1]) and (i == len(nums) - 1 or num > nums[i + 1]):
                return i
        return -1
