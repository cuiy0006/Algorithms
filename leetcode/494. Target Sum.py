class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if S > total:
            return 0
        dp = [0] * (2 * total + 1)
        dp[total] = 1
        for i, num in enumerate(nums):
            tmp = [0] * (2 * total + 1)
            for j in range(2*total + 1):
                if dp[j] != 0:
                    tmp[j + num] += dp[j]
                    tmp[j - num] += dp[j]
            dp = tmp
        return dp[total + S]

    
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def helper(idx, total):
            if idx == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            plus = helper(idx+1, total + nums[idx])
            minus = helper(idx+1, total - nums[idx])
            
            return plus + minus
            
        return helper(0, 0)
