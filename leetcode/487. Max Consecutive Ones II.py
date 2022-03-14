class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], 1]
        
        res = 1
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1] + 1
            res = max(res, *dp[i])
            
        return res
