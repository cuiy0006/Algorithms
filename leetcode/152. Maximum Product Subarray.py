import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -sys.maxsize
        left = right = 1
        for i in range(len(nums)):
            left *= nums[i]
            right *= nums[len(nums) - 1 - i]
            res = max(res, left, right)
            if nums[i] == 0:
                left = 1
            if nums[len(nums) - 1 - i] == 0:
                right = 1
        return res
