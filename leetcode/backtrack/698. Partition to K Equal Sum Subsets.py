class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        each = total // k
        
        buckets = [0] * k
        nums.sort(reverse=True)
        
        def helper(idx):
            if idx == len(nums):
                return True
            
            for i in range(0, len(buckets)):
                if buckets[i] + nums[idx] <= each:
                    buckets[i] += nums[idx]
                    if helper(idx+1):
                        return True
                    buckets[i] -= nums[idx]
                    if buckets[i] == 0:
                        return False
                if buckets[i] + nums[idx] == each:
                    return False
            return False
        
        return helper(0)