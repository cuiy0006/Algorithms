import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -sys.maxsize
        min_val = max_val = 1
        for num in nums:
            max_n = max_val * num
            min_n = min_val * num
            max_val = max(num, max_n, min_n)
            min_val = min(num, max_n, min_n)
            res = max(res, max_val)
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
