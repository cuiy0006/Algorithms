class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_val = sum(nums)
        if sum_val % k != 0:
            return False
        target = sum_val // k
        visited = [False] * 16

        def helper(lower, curr_sum, curr_k):
            if curr_k == k:
                return True
            elif curr_sum > target:
                return False
            
            last = -1    
            for i in range(lower, len(nums)):
                num = nums[i]
                
                if visited[i]:
                    continue
                
                visited[i] = True
                
                if curr_sum + num == target:
                    if helper(i + 1, 0, curr_k + 1):
                        return True
                else:
                    if helper(0, curr_sum + num, curr_k):
                        return True
                visited[i] = False
                    
            return False
        
        return helper(0, 0, 0)

      
      
      
      
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_val = sum(nums)
        if sum_val % k != 0:
            return False
        target = sum_val // k
        
        dp = [0] * k
        nums.sort(reverse=True)
        
        def helper(i):
            if i == len(nums):
                return True
            
            for j in range(0, k):
                if nums[i] + dp[j] > target:
                    continue
                dp[j] += nums[i]
                if helper(i+1):
                    return True
                dp[j] -= nums[i]
                if dp[j] == 0:
                    break

            return False
        
        return helper(0)
