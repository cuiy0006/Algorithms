class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(left, right):
            size = right - left + 1
            dp = [[0, 0] for i in range(size)]
            
            dp[0] = [0, nums[left]]
            for i in range(left+1, right+1):
                idx = i - left
                dp[idx][0] = max(dp[idx-1][0], dp[idx-1][1])
                dp[idx][1] = nums[i] + dp[idx-1][0]
                
            return max(dp[-1][0], dp[-1][1])
        
        return max(rob_range(0, len(nums)-2), rob_range(1, len(nums)-1))
