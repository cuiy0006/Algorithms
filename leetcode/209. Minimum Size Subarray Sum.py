class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        curr = 0
        res = sys.maxsize
        while j < len(nums):
            curr += nums[j]
            while curr >= target:
                res = min(res, j-i+1)
                curr -= nums[i]
                i += 1
            j += 1
        return res if res != sys.maxsize else 0
