class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 0 - increase sequence with current element as last
        # 1 - decrease sequence with current element as last
        dp = [[1, 1] for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                dp[i][1] = max(dp[i-1][0] + 1, dp[i-1][1])
            elif nums[i] > nums[i-1]:
                dp[i][0] = max(dp[i-1][1] + 1, dp[i-1][0])
            else:
                dp[i][0], dp[i][1] = dp[i-1][0], dp[i-1][1]
            
        return max(dp[-1])
