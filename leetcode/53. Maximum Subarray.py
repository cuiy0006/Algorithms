class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = -sys.maxsize
        curr = 0
        for i, num in enumerate(nums):
            curr += num
            maxVal = max(maxVal, curr)
            if curr < 0:
                curr = 0
        return maxVal

    
    
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -sys.maxsize
        min_val = max_val = 0
        for num in nums:
            max_n = max_val + num
            min_n = min_val + num
            max_val = max(num, max_n, min_n)
            min_val = min(num, max_n, min_n)
            res = max(res, max_val)
        return res
