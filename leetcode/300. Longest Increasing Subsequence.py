class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        lst = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > lst[-1]:
                lst.append(nums[i])
                continue
            left = 0
            right = len(lst)
            while left < right:
                mid = (left + right) // 2
                if lst[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1
            lst[left] = nums[i]
        return len(lst)

    
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)
