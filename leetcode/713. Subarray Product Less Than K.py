class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        i = 0
        j = 0
        curr = 1
        
        while j < len(nums):
            curr *= nums[j]
            if curr >= k:
                while i <= j and curr >= k:
                    curr /= nums[i]
                    i += 1
            cnt += j - i + 1
            j += 1
            
        return cnt
