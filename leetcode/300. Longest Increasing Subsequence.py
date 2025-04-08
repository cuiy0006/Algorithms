class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for num in nums:
            i = 0
            j = len(seq)
            while i < j:
                mid = (i+j)//2
                if seq[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            if i == len(seq):
                seq.append(num)
            else:
                seq[i] = num
        
        return len(seq)

    
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)
