class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [[1, 1] for i in range(len(nums))] # [1, 1] length of Longest Increasing Subsequence, how many combination to reach this length
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    if dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
                    elif dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                        
        maxcnt = max(dp, key=lambda x:x[0])[0]
        cnt = 0
        for d in dp:
            if d[0] == maxcnt:
                cnt += d[1]
        return cnt
