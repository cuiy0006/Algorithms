class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2, len(nums)):
            if i == 2:
                dp[i] = nums[i] + dp[0]
            else:
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        return max(dp[-1], dp[-2])

    
    
    
    
    
 class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for i in range(len(nums))]
        dp[0] = [0, nums[0]]
        
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = nums[i] + dp[i-1][0]
        
        return max(dp[-1][0], dp[-1][1])
