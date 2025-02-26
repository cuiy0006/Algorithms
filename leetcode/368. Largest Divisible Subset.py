class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        last = [i for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        last[i] = j
        
        max_len = 0
        max_idx = -1
        for i, l in enumerate(dp):
            if l > max_len:
                max_len = l
                max_idx = i
        res = []
        i = max_idx
        while last[i] != i:
            res.append(nums[i])
            i = last[i]
        res.append(nums[i])
        return res
