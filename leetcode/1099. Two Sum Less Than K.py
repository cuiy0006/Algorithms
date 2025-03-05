class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        res = -1
        while l < r:
            total = nums[l] + nums[r]
            if total < k:
                res = max(res, total)
                l += 1
            else:
                r -= 1
        return res
