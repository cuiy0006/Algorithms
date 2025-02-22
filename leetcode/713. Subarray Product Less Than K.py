class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        i = 0
        j = 0
        curr = 1
        res = 0
        while j < len(nums):
            curr *= nums[j]
            while curr >= k:
                curr /= nums[i]
                i += 1
            res += j - i + 1
            j += 1
        return res
