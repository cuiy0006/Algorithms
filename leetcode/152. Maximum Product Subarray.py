class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = nums[0]
        minVal = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            maxVal, minVal = max(num, num * minVal, num * maxVal), min(num, num * minVal, num * maxVal)
            res = max(res, maxVal)
        return res

    
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[1 for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]
        
        max_val = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i+1):
                dp[j+1][i+1] = nums[i] * dp[j+1][i]
                max_val = max(max_val, dp[j+1][i+1])
                
        return max_val
